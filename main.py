from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse
from app.crud.item import create_item, get_item, get_items, update_item, delete_item


router = APIRouter(prefix="/items", tags=["items"])

# ✅ Create
@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = create_item(db, item)
    return db_item

# ✅ Read List (pagination + optional filter by title)
@router.get("/", response_model=list[ItemResponse])
def list_items(
    skip: int = 0,
    limit: int = 10,
    title: str | None = None,
    db: Session = Depends(get_db),
):
    items = get_items(db, skip=skip, limit=limit, title=title)
    return items

# ✅ Read Single
@router.get("/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# ✅ Update (PUT)
@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    updated_item = update_item(db, item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

# ✅ Partial Update (PATCH)
@router.patch("/{item_id}", response_model=ItemResponse)
def patch_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    updated_item = update_item(db, item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

# ✅ Delete
@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    deleted_item = delete_item(db, item_id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return None
