from db import SessionLocal
from models import User, Client, Zeitbuchung, UserRole
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random

session = SessionLocal()

# --- CREATE USERS ---
users_data = [
    {"id": 1, "first_name": "Chefin", "last_name": "Chefer", "email": "chef@example.com", "hashed_password": generate_password_hash("chefpass"), "role": UserRole.Chef, "active": True},
    {"id": 2, "first_name": "Max", "last_name": "Beispiel", "email": "max@example.com", "hashed_password": generate_password_hash("maxpass"), "role": UserRole.User, "active": True},
    {"id": 3, "first_name": "Tim", "last_name": "Meispiel", "email": "tim@example.com", "hashed_password": generate_password_hash("timpass"), "role": UserRole.User, "active": True},
    {"id": 4, "first_name": "Ron", "last_name": "Peispiel", "email": "ron@example.com", "hashed_password": generate_password_hash("ronpass"), "role": UserRole.User, "active": True},
    {"id": 5, "first_name": "Mike", "last_name": "Teispiel", "email": "mike@example.com", "hashed_password": generate_password_hash("mikepass"), "role": UserRole.User, "active": True},
    {"id": 6, "first_name": "Tom", "last_name": "Reispiel", "email": "tom@example.com", "hashed_password": generate_password_hash("tompass"), "role": UserRole.User, "active": True},
]
for u in users_data:
    if not session.query(User).filter_by(id=u["id"]).first():
        session.add(User(**u))

# --- CREATE CLIENTS ---
clients_data = [
    {"id": 1, "name": "Aldi", "active": True},
    {"id": 2, "name": "Netto", "active": True},
    {"id": 3, "name": "Edeka", "active": True},
    {"id": 4, "name": "GeraArcaden", "active": True},
    {"id": 5, "name": "Action", "active": True},
]
for c in clients_data:
    if not session.query(Client).filter_by(id=c["id"]).first():
        session.add(Client(**c))

session.commit()

# --- GENERATE ZEITBUCHUNGEN ---
start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 9, 4)  # включно до 03.09.2025

for user in session.query(User).filter_by(active=True).all():
    for client in session.query(Client).filter_by(active=True).all():
        dt = start_date
        while dt < end_date:
            # Генеруємо 1 сесію щотижня для кожного user+client
            zb = Zeitbuchung(
                user_id=user.id,
                client_id=client.id,
                start_time=dt,
                end_time=dt + timedelta(hours=8),
                comment=random.choice(["Projektarbeit", "Kundenhilfe", "Urlaub"])
            )
            session.add(zb)
            dt += timedelta(days=7)
session.commit()
session.close()
print("Генерація завершена!")