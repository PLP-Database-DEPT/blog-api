from sqlmodel import select
from .models import Blog
from .schemas import BlogModel, BlogUpdateModel
from sqlmodel.ext.asyncio.session import AsyncSession

class BlogService:
    async def get_all_blogs(self, session: AsyncSession):
        statement = select(Blog).order_by(Blog.created_at)
        result = await session.exec(statement)
        return result.all()

    async def create_blog(self, blog_data: BlogModel, session: AsyncSession):
        blog_data_dict = blog_data.model_dump()
        new_blog = Blog(**blog_data_dict)
        session.add(new_blog)
        await session.commit()
        await session.refresh(new_blog)
        return new_blog

    async def get_blog(self, blog_id: str, session: AsyncSession):
        statement = select(Blog).where(Blog.id == blog_id)
        result = await session.exec(statement)
        return result.first()

    async def update_blog(self, blog_id: str, update_data: BlogUpdateModel, session: AsyncSession):
        blog = await self.get_blog(blog_id, session)
        if not blog:
            return None
        update_dict = update_data.model_dump(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(blog, key, value)
        await session.commit()
        await session.refresh(blog)
        return blog

    async def delete_blog(self, blog_id: str, session: AsyncSession):
        blog = await self.get_blog(blog_id, session)
        if not blog:
            return None
        await session.delete(blog)
        await session.commit()
        return blog
