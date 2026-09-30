import asyncio

from sqlalchemy import select

from homebase.db import AsyncSessionLocal, engine
from homebase.models import Post


async def selec1():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Post))
        return result.scalars().all()
    await engine.dispose()


print(asyncio.run(selec1()))
