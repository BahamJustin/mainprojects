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

def actionMenu():
    menu = input("""
        1. Skill Training
        2. Back To Main Menu
        
        Choose an option: """)
    
    if menu == "1":
        pass
    elif menu == "2":
        pass
    else:
        actionMenu()