from Database.schema import *
# from schema import *
import os

# db.connect()

template = "{team.city} {team.name}"

def nextSeason():
    db.connect()

    oldYear = Season.select().order_by(Season.id.desc()).get().year
    newYear = oldYear + 1

    print("Moving to next season...")

    choice = input("""
                        Confirm (Y)es or (N)o
                        
                        """)
    
    if choice == "Y" or choice == "y":
        Season.create(year=newYear)
    elif choice == "N" or choice == 'n':
        return

    db.close()

def simSeason():
    db.connect()

    oldYear = Season.select().order_by(Season.id.desc()).get().year
    newYear = oldYear + 1

    print("Are you sure you want to sim this season?")

    choice = input("""
                        Yes
                        No
                        Y or N?:""")
    
    if choice == "Y" or choice == "y":
        Season.create(year=newYear)
    elif choice == "N" or choice == 'n':
        return

    db.close()

def resetLeague():
    os.remove('league.db')

# resetLeague()

# cardinals = Team(city="Arizona", name="Cardinals", players=45)

# ravens = Team(
#     city="Baltimore",
#     name="Ravens",
# )

# Team.update(players=35).where(Team.name == "Saints").execute()

# ravens.players = 50
# ravens.save()

# ravens.delete_instance()