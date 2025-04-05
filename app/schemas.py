from pydantic import BaseModel
from typing import Optional


# ========== USER SCHEMAS ==========

class UserCreate(BaseModel):
    name: str
    skills_offered: str  # e.g., "graphic design, video editing"
    skills_wanted: str   # e.g., "python, javascript"
    location: str
    availability: str


class UserOut(BaseModel):
    id: int
    name: str
    skills_offered: str
    skills_wanted: str
    location: str
    availability: str

    class Config:
        orm_mode = True


# ========== SWAP OFFER SCHEMAS ==========

class SwapOfferCreate(BaseModel):
    user_id: int
    skill_offered: str
    skill_wanted: str
    status: Optional[str] = "open"


class SwapOfferOut(BaseModel):
    id: int
    user_id: int
    skill_offered: str
    skill_wanted: str
    status: str

    class Config:
        orm_mode = True
