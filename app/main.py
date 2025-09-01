from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers.items import router
from app.core.exceptions import add_exception_handlers

# Create DB tables
Base.metadata.create_all(bind=engine)

# FastAPI instance with docs enabled
app = FastAPI(
    title="SantectAI CRUD Service",
    version="1.0",
    docs_url="/docs",        # Swagger UI
    redoc_url="/redoc",      # ReDoc UI
    openapi_url="/openapi.json"  # OpenAPI schema
)

# Register Routers
app.include_router(router)

# Add exception handlers
add_exception_handlers(app)

@app.get("/")
def root():
    return {"message": "Welcome to SantectAI CRUD Assignment"}
