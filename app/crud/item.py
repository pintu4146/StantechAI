from sqlalchemy.orm import Session
from sqlalchemy import select
from app import models, schemas
from app.schemas.item import *
from app.models.item import *

def create_item(db: Session, item: ItemCreate):
    db_item = models.item.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 10, title: str | None = None):
    query = db.query(Item)
    if title:
        query = query.filter(Item.title.ilike(f"%{title}%"))
    return query.offset(skip).limit(limit).all()

def update_item(db: Session, item_id: int, item: schemas.ItemUpdate):
    db_item = get_item(db, item_id)
    if not db_item:
        return None
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
