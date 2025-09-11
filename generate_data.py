from db import SessionLocal
from models import User, Client, Zeitbuchung, UserRole, AuditLog, AuditActionEnum
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random
import json

session = SessionLocal()

# --- ТИПОВІ НІМЕЦЬКІ ІМЕНА І ФАМІЛІЇ ---
german_names = [
    ("Max", "Müller"),
    ("Anna", "Schmidt"),
    ("Paul", "Schneider"),
    ("Lena", "Fischer"),
    ("Tim", "Weber")
]

# --- CREATE USERS ---
users_data = []
for idx, (fname, lname) in enumerate(german_names, start=1):
    users_data.append({
        "first_name": fname,
        "last_name": lname,
        "email": f"user{idx}@axitest.de",
        "hashed_password": generate_password_hash("123456"),
        "role": UserRole.User,
        "active": True
    })

for u in users_data:
    if not session.query(User).filter_by(email=u["email"]).first():
        session.add(User(**u))

# --- CREATE CLIENTS ---
clients_data = [
    {"name": "Netto", "active": True},
    {"name": "Edeka", "active": True},
    {"name": "Aldi", "active": True},
    {"name": "GeraArkaden", "active": True},
    {"name": "Teddi", "active": True},
]
for c in clients_data:
    if not session.query(Client).filter_by(name=c["name"]).first():
        session.add(Client(**c))

session.commit()

# --- GENERATE ZEITBUCHUNGEN ---
start_date = datetime(2022, 1, 1)
end_date = datetime(2025, 9, 11)

users = session.query(User).filter_by(active=True).all()
clients = session.query(Client).filter_by(active=True).all()

zeitbuchungen = []
for user in users:
    for client in clients:
        dt = start_date
        while dt < end_date:
            zb = Zeitbuchung(
                user_id=user.id,
                client_id=client.id,
                start_time=dt,
                end_time=dt + timedelta(hours=8),
                comment=random.choice(["Projektarbeit", "Kundenhilfe", "Urlaub"])
            )
            session.add(zb)
            zeitbuchungen.append(zb)
            dt += timedelta(days=7)
session.commit()

# --- GENERATE AUDIT LOGS ---
actions = [AuditActionEnum.edit, AuditActionEnum.delete, AuditActionEnum.nachbuchung]
zeitbuchungen_all = session.query(Zeitbuchung).all()
for i in range(20):  # 20 записів аудиту
    zb = random.choice(zeitbuchungen_all)
    user = random.choice(users)
    action = random.choice(actions)
    details_dict = {
        "old": {"comment": zb.comment, "end_time": zb.end_time.strftime("%Y-%m-%d %H:%M:%S")},
        "new": {"comment": zb.comment + " (geändert)", "end_time": (zb.end_time + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")}
    }
    audit = AuditLog(
        timestamp=datetime.utcnow() - timedelta(days=random.randint(0, 30)),
        user_id=user.id,
        session_id=zb.id,
        action=action.value,
        details=json.dumps(details_dict)
    )
    session.add(audit)
session.commit()
session.close()
print("Генерація завершена!")