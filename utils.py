<<<<<<< HEAD
import re
from datetime import datetime

def sortiereListe(liste):
    "Сортує список по зростанню."
    return sorted(liste)

def parse_dt(val):
    """
    Приймає рядок дати/часу та повертає datetime-об'єкт.
    Дозволяє формати:
      - "YYYY-MM-DD HH:MM:SS"
      - "YYYY-MM-DD HH:MM"
    Якщо формат не підходить — кидає ValueError.
    """
    if val:
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
            try:
                return datetime.strptime(val, fmt)
            except ValueError:
                continue
        raise ValueError(f"Ungültiges Datum/Zeit: {val}")
    return None

def validate_email(email):
    """Проста перевірка e-mail."""
    if not email:
        return False
    # Дуже базова валідація
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def passwords_match(pw1, pw2):
    """Чи співпадають паролі і чи не пусті."""
    return pw1 and pw2 and pw1 == pw2

def strong_password(password, min_length=6):
    """Чи пароль достатньої довжини?"""
    return password is not None and len(password) >= min_length

def is_nonempty_string(s):
    """Чи це непорожній рядок (не з пробілами)?"""
    return isinstance(s, str) and s.strip() != ""

def hours_between(dt_start, dt_end):
    """Повертає кількість годин між двома datetime."""
    if not (dt_start and dt_end):
        return 0
    seconds = (dt_end - dt_start).total_seconds()
    return round(seconds / 3600, 2) if seconds > 0 else 0

def format_date(dt):
    """Форматує дату як dd.mm.yyyy"""
    if not dt:
        return ""
    return dt.strftime("%d.%m.%Y")

def is_valid_id(val):
    """Чи це валідний ID (ціле число > 0)?"""
    try:
        return int(val) > 0
    except Exception:
        return False
=======
def sortiereListe(liste, key=None, reverse=False):
    return sorted(liste, key=key, reverse=reverse)
>>>>>>> feature_audit
