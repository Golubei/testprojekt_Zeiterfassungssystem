from sqlalchemy.orm import Session
from models import User

def get_user_role(db: Session, user_email: str) -> str:
    user = db.query(User).filter(User.email == user_email).first()
    if user:
        return user.role
    return "Gast"