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

# ----------------- CHEF DASHBOARD -----------------
@app.route("/chef/dashboard", methods=["GET", "POST"])
@login_required
def chef_dashboard():
    if not session.get("user_id") or session.get("user_role") != "Chef":
        flash("Der Zugriff ist verweigert!", "danger")
        return redirect(url_for("login"))
    db = SessionLocal()
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
        elif "create_client" in request.form:
            name = request.form.get("name")
            if db.query(Client).filter(Client.name == name).first():
                flash("Ein Client mit diesem Namen existiert bereits.", "danger")
                client_form_visible = True
            else:
                new_client = Client(name=name, active=True)
                db.add(new_client)
                db.commit()
                flash("Der Client wurde erstellt!", "success")
    clients = db.query(Client).filter_by(active=True).order_by(Client.name).all()
    users = db.query(User).filter_by(active=True).order_by(User.last_name, User.first_name).all()
    clients_dict = [{"id": c.id, "name": c.name} for c in clients]
    users_dict = [{"id": u.id, "name": f"{u.first_name} {u.last_name}"} for u in users]
    # Сесія самого шефа!
    active_session = db.query(Zeitbuchung).filter_by(
        user_id=current_user.id, end_time=None
    ).order_by(Zeitbuchung.start_time.desc()).first()
    now = datetime.now()
    db.close()
    return render_template(
        "chef_dashboard.html",
        user_form_visible=user_form_visible,
        client_form_visible=client_form_visible,
        clients=clients_dict,
        users=users_dict,
        active_session=active_session,
        now=now,
        user_role="Chef"
    )

@app.route("/dashboard")
@login_required
def dashboard():
    db = SessionLocal()
    try:
        clients = db.query(Client).filter_by(active=True).order_by(Client.name).all()
        clients_dict = [{"id": c.id, "name": c.name} for c in clients]
        active_session = db.query(Zeitbuchung).filter_by(
            user_id=current_user.id, end_time=None
        ).order_by(Zeitbuchung.start_time.desc()).first()
        now = datetime.now()
        return render_template(
            'dashboard.html',
            clients=clients_dict,
            active_session=active_session,
            now=now,
            user_role="User"
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

@app.route('/api/users')
@login_required
def api_users():
    db = SessionLocal()
    try:
        users = db.query(User).filter_by(active=True).order_by(User.last_name, User.first_name).all()
        return jsonify([{"id": u.id, "name": f"{u.first_name} {u.last_name}"} for u in users])
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
        # Завжди для current_user!
        open_session = db.query(Zeitbuchung).filter_by(
            user_id=current_user.id, end_time=None
        ).first()
        if open_session:
            return jsonify({"success": False, "error": "Es gibt eine offene Sitzung"}), 400
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
        zb = db.query(Zeitbuchung).filter_by(id=session_id).first()
        if not zb or zb.end_time:
            return jsonify({"success": False, "error": "Session not found or already ended"}), 400
        if zb.user_id != current_user.id and current_user.role.value != "Chef":
            return jsonify({"success": False, "error": "Nicht erlaubt"}), 403
        zb.end_time = datetime.now()
        db.commit()
        return jsonify({"success": True, "session_id": zb.id})
    finally:
        db.close()

@app.route('/api/finish_session', methods=['POST'])
@login_required
def api_finish_session():
    db = SessionLocal()
    try:
        session_id = request.json.get("session_id")
        comment = request.json.get("comment", "")
        zb = db.query(Zeitbuchung).filter_by(id=session_id).first()
        if not zb or not zb.end_time:
            return jsonify({"success": False, "error": "Session not ended"}), 400
        if zb.user_id != current_user.id and current_user.role.value != "Chef":
            return jsonify({"success": False, "error": "Nicht erlaubt"}), 403
        if not comment.strip():
            return jsonify({"success": False, "error": "Kommentar erforderlich"}), 400
        zb.comment = comment
        db.commit()
        return jsonify({"success": True})
    finally:
        db.close()

@app.route('/api/session_history')
@login_required
def api_session_history():
    user_id = request.args.get("user_id", type=int)
    client_id = request.args.get("client_id", type=int)
    # Нове!
    start_date = request.args.get("start_date")  # формат: 'YYYY-MM-DD'
    end_date = request.args.get("end_date")      # формат: 'YYYY-MM-DD'

    db = SessionLocal()
    try:
        q = db.query(Zeitbuchung)
        # --- Фільтр періоду ---
        if start_date:
            q = q.filter(Zeitbuchung.start_time >= datetime.strptime(start_date, "%Y-%m-%d"))
        if end_date:
            # до кінця дня
            q = q.filter(Zeitbuchung.start_time <= datetime.strptime(end_date, "%Y-%m-%d").replace(hour=23, minute=59, second=59))
        # --- Фільтр юзера ---
        if current_user.role.value == "Chef":
            if user_id:
                q = q.filter(Zeitbuchung.user_id == user_id)
        else:
            q = q.filter(Zeitbuchung.user_id == current_user.id)
        # --- Фільтр клієнта ---
        if client_id:
            q = q.filter(Zeitbuchung.client_id == client_id)
        q = q.order_by(Zeitbuchung.start_time.desc())
        result = []
        for s in q:
            result.append({
                "id": s.id,
                "user_id": s.user.id,
                "user": f"{s.user.first_name} {s.user.last_name}",
                "client": s.client.name,
                "start_time": s.start_time.strftime('%Y-%m-%d %H:%M:%S'),
                "end_time": s.end_time.strftime('%Y-%m-%d %H:%M:%S') if s.end_time else "",
                "comment": s.comment or ""
            })
        return jsonify(result)
    finally:
        db.close()

@app.route('/api/nachbuchung', methods=['POST'])
@login_required
def api_nachbuchung():
    db = SessionLocal()
    try:
        data = request.get_json(force=True)  # force=True щоб завжди парсив JSON

        # 1. Визначаємо user_id
        if current_user.role.value == "Chef":
            user_id_raw = data.get("user_id")
            if not user_id_raw or str(user_id_raw).strip() == "":
                return jsonify({"success": False, "error": "Mitarbeiter wählen!"}), 400
            try:
                user_id = int(user_id_raw)
            except Exception:
                return jsonify({"success": False, "error": "Ungültige Mitarbeiter-ID!"}), 400
            # Перевіряємо, що юзер існує та активний
            user = db.query(User).filter_by(id=user_id, active=True).first()
            if not user:
                return jsonify({"success": False, "error": "Mitarbeiter existiert nicht!"}), 400
        else:
            user_id = current_user.id

        # 2. client_id
        client_id_raw = data.get("client_id")
        if not client_id_raw or str(client_id_raw).strip() == "":
            return jsonify({"success": False, "error": "Kunde wählen!"}), 400
        try:
            client_id = int(client_id_raw)
        except Exception:
            return jsonify({"success": False, "error": "Ungültige Kunden-ID!"}), 400
        # перевіряємо, що клієнт існує та активний
        client = db.query(Client).filter_by(id=client_id, active=True).first()
        if not client:
            return jsonify({"success": False, "error": "Kunde existiert nicht!"}), 400

        # 3. Дати/час
        start_time = data.get("start_time")
        end_time = data.get("end_time")
        comment = data.get("comment", "")

        # 4. Перевірка обов'язкових полів
        if not all([user_id, client_id, start_time, end_time, comment.strip()]):
            return jsonify({"success": False, "error": "Alle Felder sind Pflichtfelder!"}), 400

        # 5. Дата-час формат
        try:
            dt_start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            dt_end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        except Exception:
            return jsonify({"success": False, "error": "Ungültiges Datum/Zeit!"}), 400

        # 6. Перевірка: чи кінець після початку
        if dt_start >= dt_end:
            return jsonify({"success": False, "error": "Beginn muss vor Ende liegen!"}), 400

        # 7. (Опціонально) Чи не перетинається з іншими Buchungen? Тут можна додати перевірку, якщо потрібно

        # 8. Створення записи
        zb = Zeitbuchung(
            user_id=user_id,
            client_id=client_id,
            start_time=dt_start,
            end_time=dt_end,
            comment=comment.strip()
        )
        db.add(zb)
        db.commit()
        return jsonify({"success": True})
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return jsonify({"success": False, "error": f"Interner Fehler: {str(e)}"}), 500

@app.route('/api/session/<int:session_id>', methods=['PUT'])
@login_required
def api_edit_session(session_id):
    db = SessionLocal()
    try:
        zb = db.query(Zeitbuchung).filter_by(id=session_id).first()
        if not zb:
            return jsonify({'success': False, 'error': 'Sitzung nicht gefunden'}), 404
        now = datetime.now()
        if current_user.role.value != "Chef":
            if zb.user_id != current_user.id:
                return jsonify({'success': False, 'error': 'Nicht erlaubt'}), 403
            # Перевіряємо, що оригінальна сесія у поточному місяці
            if zb.start_time.month != now.month or zb.start_time.year != now.year:
                return jsonify({'success': False, 'error': 'Nicht erlaubt'}), 403
        data = request.get_json()
        # --- Перевірка зміни місяця для User ---
        if current_user.role.value != "Chef":
            # Який місяць дозволено
            allowed_month = now.month
            allowed_year = now.year
            # старт
            new_start_time = zb.start_time
            if 'start_time' in data:
                new_start_time = datetime.strptime(data['start_time'], "%Y-%m-%d %H:%M:%S")
            # кінець (може бути порожнім)
            new_end_time = zb.end_time
            if 'end_time' in data:
                if data['end_time']:
                    new_end_time = datetime.strptime(data['end_time'], "%Y-%m-%d %H:%M:%S")
                else:
                    new_end_time = None
            # Якщо змінюється місяць — заборонити
            if (new_start_time.month != allowed_month or new_start_time.year != allowed_year) or (new_end_time and (new_end_time.month != allowed_month or new_end_time.year != allowed_year)):
                return jsonify({'success': False, 'error': 'Bearbeitungsfehler! Änderungen sind nur im Kalendermonat möglich!'}), 400
        # --- Оновлення ---
        if 'client_id' in data:
            zb.client_id = int(data['client_id'])
        if 'start_time' in data:
            zb.start_time = datetime.strptime(data['start_time'], "%Y-%m-%d %H:%M:%S")
        if 'end_time' in data:
            if data['end_time']:
                zb.end_time = datetime.strptime(data['end_time'], "%Y-%m-%d %H:%M:%S")
            else:
                zb.end_time = None
        if 'comment' in data:
            zb.comment = data['comment']
        db.commit()
        return jsonify({'success': True})
    finally:
        db.close()

@app.route('/api/session/<int:session_id>', methods=['DELETE'])
@login_required
def api_delete_session(session_id):
    db = SessionLocal()
    try:
        zb = db.query(Zeitbuchung).filter_by(id=session_id).first()
        if not zb:
            return jsonify({'success': False, 'error': 'Sitzung nicht gefunden'}), 404
        now = datetime.now()
        if current_user.role.value != "Chef":
            if zb.user_id != current_user.id:
                return jsonify({'success': False, 'error': 'Nicht erlaubt'}), 403
            if zb.start_time.month != now.month or zb.start_time.year != now.year:
                return jsonify({'success': False, 'error': 'Nicht erlaubt'}), 403
        db.delete(zb)
        db.commit()
        return jsonify({'success': True})

    finally:
        db.close()

if __name__ == "__main__":
    app.run(debug=True)

