from peewee import *
from pathlib import Path
import csv
import sys
import os
import random
from consolemenu import *
from consolemenu import SelectionMenu
from consolemenu.items import *
from Database.createData import *
from Database.readData import *
from Database.updateData import *
import psycopg2


def skillMenu():
    if User.get().forceSensitivity == 1:
        playerForceSense = "Yes"
    else:
        playerForceSense = "No"

    user = User.get()

    skillInfo = f"""
        Force Sensitivty: {playerForceSense}
        Force Skill: {user.forceSkill}
        Melee: {user.meleeSkill}
        Ranged: {user.rangedSkill}
        Agility: {user.agilitySkill}
        Piloting: {user.pilotingSkill}
        Stealth: {user.stealthSkill}
        Trade: {user.tradeSkill}
        Smuggling: {user.smugglingSkill}
        Leadership: {user.leadershipSkill}
        Strategy: {user.strategySkill}
        Medical: {user.medicalSkill}
        Tracking: {user.trackingSkill}
        Slicing: {user.slicingSkill}
        Engineering: {user.engineeringSkill}"""
    print("")
    print(skillInfo)

    Screen().input('Press [Enter] to continue')

    pg_db.close()


def playerCard():
    # add player skills, then item skill bonuses, then equipment, add skill bonuses
    user = User.get_by_id(1)

    # more player info - companions?
    playerInfo = f"""
        Name: {user.name} {user.familyName} 
        Age: {user.age}                     
        Race: {user.race}
        Home Planet: {user.homePlanet}"""
    print(playerInfo)

    # add an inventory
    # add equiupment - ability to equip items
    # check skill numbers
    charMenu = input("""
        1. Inventory
        2. Equipment
        3. Skills
        4. Back to Main Menu
        
        Choose an option: """)

    if charMenu == "1":
        getInventory()
        playerCard()
    elif charMenu == "2":
        pass
    elif charMenu == "3":
        skillMenu()
        playerCard()
    elif charMenu == "4":
        pass
    else:
        playerCard()