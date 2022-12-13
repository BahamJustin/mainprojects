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

def relationMenu():
    userDetails = User.get()
    playerFamily = userDetails.familyName

    menu = input("""
        1. View Family
        2. Friends/Rivals
        3. All
        4. Search
        5. Back to Main Menu
        
        Choose an option: """)

    if menu == "1":
        print("")
        viewFamily(playerFamily)
    elif menu == "2":
        pass
    elif menu == "3":
        pass
    elif menu == "4":
        pass
    elif menu == "5":
        pass
    else:
        relationMenu()