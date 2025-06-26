from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db import initdb
from src.routes import router as blog_router  



@asynccontextmanager
async def lifespan(app: FastAPI):
    await initdb() 
    yield

app = FastAPI(
    title="Blog API",
    description="A simple RESTful API for software testing class",
    lifespan=lifespan
)

app.include_router(blog_router)  


@app.get("/")
def home():
    return  {"msg": "Hello World"}
