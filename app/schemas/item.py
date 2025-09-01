from pydantic import BaseModel
from datetime import datetime

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    title: str | None = None
    description: str | None = None

class ItemResponse(ItemBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
