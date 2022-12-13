import os
from Database.schema import *
from os import *
import random
import names
from consolemenu import *
from consolemenu.items import *
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def advanceTime():
    # print("-" * 35)

    if Date.get().month >= 12:
        Date.update(month=1).execute()
        Date.update(year=Date.year + 1).execute()
        # print(Date.get().month, "is greater than 12")
    else:
        Date.update(month=Date.month + 1).execute()
        # print(Date.get().month, "is less than 12")
        
        

    # Screen().input('Press [Enter] to continue')

    pg_db.close()