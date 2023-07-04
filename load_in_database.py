import asyncio
import csv
from models import engine, Session, StarHeroes


async def load_data():
    with open("heroes_star.csv", "r") as file:
        reader = csv.DictReader(file)
        async with Session() as session:
            async with engine.begin() as conn:
                for row in reader:
                    hero = StarHeroes(
                        name=row["name"],
                        birth_year=row["birth_year"],
                        eye_color=row["eye_color"],
                        films=row["films"],
                        gender=row["gender"],
                        hair_color=row["hair_color"],
                        height=row["height"],
                        homeworld=row["homeworld"],
                        mass=row["mass"],
                        skin_color=row["skin_color"],
                        species=row["species"],
                        starships=row["starships"],
                        vehicles=row["vehicles"],
                    )
                    session.add(hero)
                await session.commit()


asyncio.run(load_data())
