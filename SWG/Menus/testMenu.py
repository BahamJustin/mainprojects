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

def testMenu():
    testMenu = input("""
        1. Advance Time
        2. Add Inventory
        3. Remove Inventory
        4. View Inventory
        5. Back to Main Menu
        
        Choose an option: """)

    if testMenu == "1":
        advanceTime()
    elif testMenu == "2":
        randItems()
    elif testMenu == "3":
        pass
    elif testMenu == "4":
        getInventory()
    elif testMenu == "5":
        pass
    else:
        pass