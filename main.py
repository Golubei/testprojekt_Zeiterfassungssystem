from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, UserRole, Client, Zeitbuchung
from db import SessionLocal, Base, engine
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    db = SessionLocal()
    user = db.query(User).get(int(user_id))
    db.close()
    return user

# Create all tables
Base.metadata.create_all(bind=engine)

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    db = SessionLocal()
    chef = db.query(User).filter(User.role == UserRole.Chef).first()
    db.close()
    if chef:
        flash("Ein Teamleiter existiert bereits.", "warning")
        return redirect(url_for("login"))
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        db = SessionLocal()
        if db.query(User).filter(User.email == email).first():
            flash("Diese E-Mail-Adresse ist bereits vergeben.", "danger")
            db.close()
            return render_template("register.html")
        if password != password2:
            flash("Passwörter stimmen nicht überein.", "danger")
            db.close()
            return render_template("register.html")
        if not (email and first_name and last_name and password):
            flash("Bitte alle Felder ausfüllen.", "danger")
            db.close()
            return render_template("register.html")
        hashed_password = generate_password_hash(password)
        new_chef = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            hashed_password=hashed_password,
            role=UserRole.Chef,
            active=True,
        )
        db.add(new_chef)
        db.commit()
        db.close()
        flash("Teamleiter erfolgreich registriert! Sie können sich jetzt anmelden.", "success")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        db = SessionLocal()
        user = db.query(User).filter(User.email == email).first()
        db.close()
        if user and check_password_hash(user.hashed_password, password):
            login_user(user)
            session["user_id"] = user.id
            user_role = user.role.value if hasattr(user.role, 'value') else str(user.role)
            session["user_role"] = user_role
            flash("Erfolgreich eingeloggt!", "success")
            if user_role == "Chef":
                return redirect(url_for("chef_dashboard"))
            else:
                return redirect(url_for("dashboard"))
        else:
            flash("Ungültige E-Mail oder Passwort.", "danger")
    # GET або невірний логін:
    return render_template("login.html")

def send_reset_email(email):
    sender = "noreply@yourdomain.com"
    recipient = email
    subject = "Passwort zurücksetzen"
    body = "Sie haben eine Anfrage zum Zurücksetzen Ihres Passworts gestellt. Hier könnte Ihr Link stehen..."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient
    try:
        with smtplib.SMTP("localhost") as server:
            server.sendmail(sender, [recipient], msg.as_string())
    except Exception as e:
        print("Fehler beim Senden der E-Mail:", e)

@app.route("/chef/dashboard", methods=["GET", "POST"])
@login_required
def chef_dashboard():
    if not session.get("user_id") or session.get("user_role") != "Chef":
        flash("Der Zugriff ist verweigert!", "danger")
        return redirect(url_for("login"))

    user_form_visible = False
    client_form_visible = False

    if request.method == "POST":
        if "show_user_form" in request.form:
            user_form_visible = True
        elif "show_client_form" in request.form:
            client_form_visible = True
        elif "create_user" in request.form:
            email = request.form.get("email")
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            password = request.form.get("password")
            password2 = request.form.get("password2")
            db = SessionLocal()
            if db.query(User).filter(User.email == email).first():
                flash("Ein Benutzer mit dieser E-Mail existiert bereits.", "danger")
                user_form_visible = True
            elif password != password2:
                flash("Die Passwörter stimmen nicht überein.", "danger")
                user_form_visible = True
            else:
                hashed_password = generate_password_hash(password)
                new_user = User(
                    email=email,
                    hashed_password=hashed_password,
                    role=UserRole.User,
                    first_name=first_name,
                    last_name=last_name,
                    active=True,
                )
                db.add(new_user)
                db.commit()
                flash("Mitarbeiter erstellt!", "success")
            db.close()
        elif "create_client" in request.form:
            name = request.form.get("name")
            db = SessionLocal()
            if db.query(Client).filter(Client.name == name).first():
                flash("Ein Client mit diesem Namen existiert bereits.", "danger")
                client_form_visible = True
            else:
                new_client = Client(name=name, active=True)
                db.add(new_client)
                db.commit()
                flash("Der Client wurde erstellt!", "success")
            db.close()

    return render_template(
        "chef_dashboard.html",
        user_form_visible=user_form_visible,
        client_form_visible=client_form_visible,
    )

@app.route("/dashboard")
@login_required
def dashboard():
    db = SessionLocal()
    try:
        clients = db.query(Client).filter_by(active=True).order_by(Client.name).all()
        active_session = db.query(Zeitbuchung).filter_by(
            user_id=current_user.id, end_time=None
        ).order_by(Zeitbuchung.start_time.desc()).first()
        now = datetime.now()
        month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        session_history = db.query(Zeitbuchung).filter(
            Zeitbuchung.user_id == current_user.id,
            Zeitbuchung.start_time >= month_start
        ).order_by(Zeitbuchung.start_time.desc()).all()
        return render_template(
            'dashboard.html',
            clients=clients,
            active_session=active_session,
            session_history=session_history,
            now=now
        )
    finally:
        db.close()

@app.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    flash("Erfolgreich ausgeloggt.", "success")
    return redirect(url_for("login"))

@app.route('/api/clients')
@login_required
def api_clients():
    db = SessionLocal()
    try:
        clients = db.query(Client).filter_by(active=True).order_by(Client.name).all()
        return jsonify([{"id": c.id, "name": c.name} for c in clients])
    finally:
        db.close()

@app.route('/api/start_session', methods=['POST'])
@login_required
def api_start_session():
    db = SessionLocal()
    try:
        client_id = request.json.get("client_id")
        if not client_id:
            return jsonify({"success": False, "error": "No client selected"}), 400
        open_session = db.query(Zeitbuchung).filter_by(
            user_id=current_user.id, end_time=None
        ).first()
        if open_session:
            return jsonify({"success": False, "error": "You have unfinished session"}), 400
        zb = Zeitbuchung(
            user_id=current_user.id,
            client_id=client_id,
            start_time=datetime.now()
        )
        db.add(zb)
        db.commit()
        db.refresh(zb)
        return jsonify({"success": True, "session_id": zb.id, "start_time": zb.start_time.isoformat()})
    finally:
        db.close()

@app.route('/api/end_session', methods=['POST'])
@login_required
def api_end_session():
    db = SessionLocal()
    try:
        session_id = request.json.get("session_id")
        zb = db.query(Zeitbuchung).filter_by(id=session_id, user_id=current_user.id).first()
        if not zb or zb.end_time:
            return jsonify({"success": False, "error": "Session not found or already ended"}), 400
        zb.end_time = datetime.now()
        db.commit()
        return jsonify({"success": True, "end_time": zb.end_time.isoformat()})
    finally:
        db.close()

@app.route('/api/finish_session', methods=['POST'])
@login_required
def api_finish_session():
    db = SessionLocal()
    try:
        session_id = request.json.get("session_id")
        comment = request.json.get("comment", "")
        zb = db.query(Zeitbuchung).filter_by(id=session_id, user_id=current_user.id).first()
        if not zb or not zb.end_time:
            return jsonify({"success": False, "error": "Session not ended"}), 400
        zb.comment = comment
        db.commit()
        return jsonify({"success": True})
    finally:
        db.close()

@app.route('/api/session_history')
@login_required
def api_session_history():
    db = SessionLocal()
    try:
        now = datetime.now()
        month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        history = db.query(Zeitbuchung).filter(
            Zeitbuchung.user_id == current_user.id,
            Zeitbuchung.start_time >= month_start
        ).order_by(Zeitbuchung.start_time.desc()).all()
        result = []
        for s in history:
            result.append({
                "id": s.id,
                "client": s.client.name,
                "start_time": s.start_time.strftime('%Y-%m-%d %H:%M:%S'),
                "end_time": s.end_time.strftime('%Y-%m-%d %H:%M:%S') if s.end_time else None,
                "comment": s.comment or ""
            })
        return jsonify(result)
    finally:
        db.close()

if __name__ == "__main__":
    app.run(debug=True)