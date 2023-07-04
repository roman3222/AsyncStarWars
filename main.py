import asyncio
import aiohttp
from more_itertools import chunked
import csv


async def get_heroes():
    session = aiohttp.ClientSession()
    response = await session.get("https://swapi.dev/api/people/")
    json_data = await response.json()
    await session.close()
    return json_data["results"]


def record_in_file(data):
    with open("heroes_star.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "name",
                "birth_year",
                "eye_color",
                "films",
                "gender",
                "hair_color",
                "height",
                "homeworld",
                "mass",
                "skin_color",
                "species",
                "starships",
                "vehicles",
            ]
        )
        for person in data:
            species = ", ".join(person["species"])
            starships = ", ".join(person["starships"])
            vehicles = ", ".join(person["vehicles"])
            films = ", ".join(person["films"])
            writer.writerow(
                [
                    person["name"],
                    person["birth_year"],
                    person["eye_color"],
                    films,
                    person["gender"],
                    person["hair_color"],
                    person["height"],
                    person["homeworld"],
                    person["mass"],
                    person["skin_color"],
                    species,
                    starships,
                    vehicles,
                ]
            )


async def main():
    heroes = await get_heroes()
    record_in_file(heroes)


if __name__ == "__main__":
    asyncio.run(main())
