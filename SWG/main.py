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
from Menus.playerCard import *
from Menus.relationMenu import *
from Menus.testMenu import *
import psycopg2

def createUser():
    # random gen names
    name = input("Enter your name: ")

    familyName = input("Enter Your Family Name: ")

    # add more races - race stat bonuses
    race = input("""
        1.Human     2.Human
        2.Human     3.Human
        3.Human     4.Human
        
        Choose a race: """)

    # make genuine list of planets - planet bonuses
    homePlanet = input("""
        1.Tatooine      2.Jakku
        3.Geonosis      4.Pasana
        5.Savareen      6.Jedha
        
        Choose a planet: """)

    if name.strip() == "" or race.strip == "" or homePlanet.strip() == "":
        print("dumbass")
        createUser()
    else:
        newUser(name, familyName, race, homePlanet)

def newGameMenu():
    print("Are You Sure?")

    choice = input("""
        Confirm (Y)es or (N)o: """)
    
    if choice == "Y" or choice == "y":
        newGame()
        createUser()
    elif choice == "N" or choice == 'n':
        return
    else:
        print("dumbass")
        newGameMenu()

def homeMenu():
    print("")
    print("S.W.G")
    print("")
    try:
        getDate()
    except:
        pass

    # Current situation Info on homeMenu screen

    # Settlement menu - locations
    #  Action menu?
    choice = input("""
        1. My Character
        2. Relationships
        3. Actions
        4. Planet
        D: Dev Test
        N. New Game?
        Q: Exit Game

        Please enter your choice: """)

    if choice == "1":
        playerCard()
        homeMenu()
    elif choice == "2":
        relationMenu()
        homeMenu()
    elif choice == "3":
        pass
    elif choice == "D" or choice == "d":
        testMenu()
        homeMenu()
    elif choice == "N" or choice == "n":
        newGameMenu()
        homeMenu()
    elif choice == "q" or choice == "Q":
        pass
    else:
        print("dumbass")
        homeMenu()

def databaseExist():
    connection = None
    try:
        connection = psycopg2.connect(host='localhost', user='postgres', password='Saints504!')
    except:
        print('Database not connected.')

    if connection is not None:
        connection.autocommit = True

        cur = connection.cursor()

        cur.execute("SELECT datname FROM pg_database;")

        list_database = cur.fetchall()

        if ("galaxy") in list_database:
            print("Galaxy Loaded")
            homeMenu()
        else:
            print("Starting a new game")
            newGame()
            createUser()
            homeMenu()
        connection.close()

def startGame():
    print("Checking for Galaxy")
    databaseExist()

def kivyTest():
    try:
        getDate()
    except:
        pass

def main():
   pass

if __name__ == '__main__':
    startGame()