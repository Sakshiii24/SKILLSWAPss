from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, ml_matcher

router = APIRouter(prefix="/match", tags=["match"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{user_id}")
def get_matches(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    all_offers = crud.get_all_swap_offers(db)
    matches = ml_matcher.get_best_matches(user.skills_offered, all_offers)
    return {"matches": [
        {
            "offer_id": o.id,
            "skill_offered": o.skill_offered,
            "skill_wanted": o.skill_wanted,
            "user_id": o.user_id
        } for o, _ in matches
    ]}
