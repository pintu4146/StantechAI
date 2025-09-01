import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base
from app.crud import item as crud
from app.schemas.item import ItemCreate, ItemUpdate

# Setup in-memory SQLite for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_and_update_item(db):
    # Create item
    item_in = ItemCreate(title="UnitTest Book", description="Initial desc")
    created_item = crud.create_item(db, item_in)
    assert created_item.title == "UnitTest Book"

    # Update item
    update_in = ItemUpdate(description="Updated desc")
    updated_item = crud.update_item(db, created_item.id, update_in)
    assert updated_item.description == "Updated desc"
