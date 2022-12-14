import os
from Database.schema import *
# from schema import *
from os import *
import random
import names
import psycopg2
from skills import *
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def randNum():
    print(random.randrange(20, 65))

planets = (
    ("Tatooine"),
    ("Jakku"),
    ("Geonosis"),
    ("Pasaana"),
    ("Savareen"),
    ("Jedha")
)

race = (
    ("Human"),
    ("Twi'lek"),
    ("Togruta"),
    ("Cathar"),
)

# turn into json files?
# skills json (dont have to update in database)
items = {
    ("Body Pillow", "Misc", randSkill()),
    ("iPhone With Flappy Bird", "Misc", randSkill()),
    ("Gun", "Weapon", randSkill()),
    ("Lightsaber", "Weapon", randSkill())
}

professions = []

factions = (
    ("Galactic Empire"),
    ("Rebel Alliance"),
    ("Hutt Cartel")
)

events = (
    ("a"),
    ("b"),
    ("c")
)

playerinventory = []

models = ([Planet, Settlement, Actor, Item, Faction, Event, User, PlayerInventory, Date])

def newDatabase():
    conn = psycopg2.connect(host='localhost', user='postgres', password='Saints504!')
    cur = conn.cursor()

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur.execute("DROP TABLE IF EXISTS Planet, Settlement, Actor, Item, Faction, Event, User, PlayerInventory, Date")
    # cur.execute('CREATE DATABASE galaxy')

    conn.close()
    
def genGalaxy():
    pg_db.drop_tables(models)

    pg_db.create_tables(models)

    for planet in planets:
        Planet.create(name=planet)
        for settlement in range(1):
            if planet == "Tatooine":
                Settlement.create(
                    name="Mos Eisley",
                    homePlanet=planet
                )
                Settlement.create(
                    name="Mos Esfa",
                    homePlanet=planet
                )
            else:
                Settlement.create(
                    name="First",
                    homePlanet=planet
                )
                Settlement.create(
                    name="Second",
                    homePlanet=planet
                )
        for actor in range(5):\
            # create star wars name gen
            Actor.create(
            name=names.get_first_name(),
            age=random.randrange(0, 101),
            familyName=names.get_last_name(),
            race=random.choice(race),
            homePlanet=planet,
            meleeSkill=random.randrange(0, 101),
            rangedSkill=random.randrange(0, 101),
            agilitySkill=random.randrange(0, 101),
            pilotingSkill=random.randrange(0, 101),
            stealthSkill=random.randrange(0, 101),
            tradeSkill=random.randrange(0, 101),
            smugglingSkill=random.randrange(0, 101),
            leadershipSkill=random.randrange(0, 101),
            strategySkill=random.randrange(0, 101),
            medicalSkill=random.randrange(0, 101),
            trackingSkill=random.randrange(0, 101),
            survivalSkill=random.randrange(0, 101),
            trappingSkill=random.randrange(0, 101),
            slicingSkill=random.randrange(0, 101),
            engineeringSkill=random.randrange(0, 101)
            )

    for item in items:
        Item.create(
            name=item[0],
            itemType = item[1],
            bonusSkill=item[2],
            inPlayerInventory=0
        )

    ### Create Factions
    for faction in factions:
        Faction.create(
            name=faction
        )

    ### Write Events
    for event in events:
        Event.create(
            name=event
        )

    ### Finalize Timeline
    Date.create(
        month=1,
        year=4
    )

    pg_db.close()

def randItems():
    # put randmisc into inventory, then view inventory
    ### Specific Items given for differnet starts
    for item in Item.select().where(Item.itemType == "Weapon").order_by(fn.Random()).limit(1):
        Item.create(
            name=item.name,
            itemType=item.itemType,
            bonusSkill=item.bonusSkill,
            inPlayerInventory=1
        )

    for item in Item.select().where(Item.itemType == "Misc").order_by(fn.Random()).limit(1):
        Item.create(
            name=item.name,
            itemType=item.itemType,
            bonusSkill=item.bonusSkill,
            inPlayerInventory=1
        )

def newUser(name, familyName, race, homePlanet):
    pg_db.drop_tables(User)
    pg_db.drop_tables(PlayerInventory)
    User.create(
        name=name,
        age=20,
        familyName=familyName,
        race=race,
        homePlanet=homePlanet,
        ### Different Starts grant different stats
        forceSensitivity=random.randrange(0, 2),
        forceSkill=random.randrange(0, 101),
        meleeSkill=random.randrange(0, 101),
        rangedSkill=random.randrange(0, 101),
        agilitySkill=random.randrange(0, 101),
        pilotingSkill=random.randrange(0, 101),
        stealthSkill=random.randrange(0, 101),
        tradeSkill=random.randrange(0, 101),
        smugglingSkill=random.randrange(0, 101),
        leadershipSkill=random.randrange(0, 101),
        strategySkill=random.randrange(0, 101),
        medicalSkill=random.randrange(0, 101),
        trackingSkill=random.randrange(0, 101),
        survivalSkill=random.randrange(0, 101),
        trappingSkill=random.randrange(0, 101),
        slicingSkill=random.randrange(0, 101),
        engineeringSkill=random.randrange(0, 101)
    )

    randItems()

    ### Specific family relationships
    for actor in range(2):
        Actor.create(
            name=names.get_first_name(),
            age=random.randrange(0, 101),
            familyName=familyName,
            race=race,
            homePlanet=homePlanet,
            meleeSkill=random.randrange(0, 101),
            rangedSkill=random.randrange(0, 101),
            agilitySkill=random.randrange(0, 101),
            pilotingSkill=random.randrange(0, 101),
            stealthSkill=random.randrange(0, 101),
            tradeSkill=random.randrange(0, 101),
            smugglingSkill=random.randrange(0, 101),
            leadershipSkill=random.randrange(0, 101),
            strategySkill=random.randrange(0, 101),
            medicalSkill=random.randrange(0, 101),
            trackingSkill=random.randrange(0, 101),
            survivalSkill=random.randrange(0, 101),
            trappingSkill=random.randrange(0, 101),
            slicingSkill=random.randrange(0, 101),
            engineeringSkill=random.randrange(0, 101)
        )

def newGame():
    # newDatabase()
    genGalaxy()