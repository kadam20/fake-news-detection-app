from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import backend.db.models as models
from backend.db.database import engine
from backend.api.routes import route
import asyncio

# Initialize FastAPI
app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(route.router)


@app.get("/")
async def root():
    return {"message": "Api works"}


async def main():
    config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
