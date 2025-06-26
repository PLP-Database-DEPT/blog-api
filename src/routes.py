from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession

from .models import Blog
from .db import get_session
from .service import BlogService
from .schemas import BlogModel, BlogUpdateModel

router = APIRouter(prefix="/blogs", tags=["Blog"])
blog_service = BlogService()

@router.get("/", response_model=List[Blog])
async def list_blog(session: AsyncSession = Depends(get_session)):
    return await blog_service.get_all_blogs(session)

@router.post("/", response_model=Blog, status_code=status.HTTP_201_CREATED)
async def create_blog(blog_data: BlogModel, session: AsyncSession = Depends(get_session)):
    return await blog_service.create_blog(blog_data, session)

@router.get("/{blog_id}", response_model=Blog)
async def retrieve_blog(blog_id: str, session: AsyncSession = Depends(get_session)):
    blog = await blog_service.get_blog(blog_id, session)
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not Found")
    return blog

@router.patch("/{blog_id}", response_model=Blog)
async def update_blog(blog_id: str, blog_data: BlogUpdateModel, session: AsyncSession = Depends(get_session)):
    blog = await blog_service.update_blog(blog_id, blog_data, session)
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not Found")
    return blog

@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(blog_id: str, session: AsyncSession = Depends(get_session)):
    deleted = await blog_service.delete_blog(blog_id, session)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Blog not Found")
    return {}
