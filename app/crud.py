from sqlalchemy.orm import Session
from app import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_all_swap_offers(db: Session):
    return db.query(models.SwapOffer).filter(models.SwapOffer.status == 'open').all()