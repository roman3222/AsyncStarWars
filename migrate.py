import asyncio

from models import engine, Base


async def migrate_data():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(migrate_data())
