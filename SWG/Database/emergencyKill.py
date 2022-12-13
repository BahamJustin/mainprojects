import os
from Database.schema import *
from os import *
import random
import names
from consolemenu import *
from consolemenu.items import *
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

models = ([Planet, Settlement, Actor, Item, Faction, Event, User, PlayerInventory, Date])


def killDatabase():
    pg_db.drop_tables(models)
    pg_db.create_tables(models)
    print("DB Killed")
    # conn = psycopg2.connect(host='localhost', user='postgres', password='Saints504!')
    # cur = conn.cursor()

    # conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # cur.execute("DROP TABLE IF EXISTS Planet, Settlement, Actor, Item, Faction, Event, User, PlayerInventory, Date")
    # conn.close()