from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=schemas.item.ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: schemas.item.ItemCreate, db: Session = Depends(get_db)):
    return crud.item.create_item(db, item)

@router.get("/", response_model=list[schemas.item.ItemResponse])
def list_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.item.get_items(db, skip, limit)

@router.get("/{item_id}", response_model=schemas.item.ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.item.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=schemas.item.ItemResponse)
def update_item(item_id: int, item: schemas.item.ItemUpdate, db: Session = Depends(get_db)):
    updated_item = crud.item.update_item(db, item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    deleted_item = crud.item.delete_item(db, item_id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return None
