from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.database import get_db
import backend.db.models as models

router = APIRouter()

@router.get("/top-tweets")
async def get_tweets(db: Session = Depends(get_db)):
    return {"Roure works"}
