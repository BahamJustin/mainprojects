from Database.schema import *
# from schema import *
from peewee import fn
import sys

teamTemplate = "{team.city} {team.name}"
actorTemplate = "{actor.firstName} {actor.lastName}"
playerTemplate = "{player.firstName} {player.lastName} {player.teamName_id} {player.position} {player.overall}"
rosterTemplate = "{player.firstName} {player.lastName} {player.position} {player.overall}"

def viewAllTeams():
    # db.connect()
    print("All Teams")
    print("-" * 35)

    ############### Need to format list better
    for team in Team.select():
        print(teamTemplate.format(team=team))
    # db.close()

# Get specific team by ID
def teamByID(ID):
    # db.connect()
    print(ID)
    print("-" * 35)

    print(Team.get_by_id(ID).name)
    # db.close()

# Specific team by name
def teamByName(Name):
    print(Name)
    print("-" * 35)

    for team in Team.select().where(Team.name == Name):
        print(teamTemplate.format(team=team))

def teamByConf(Confs):
    # db.connect()
    print(Confs)
    print("-" * 35)

    for team in Team.select().where(Team.conf == Confs):
        print(teamTemplate.format(team=team))
    # db.close()

def teamByDiv(Divs):
    # db.connect()
    print(Divs)
    print("-" * 35)

    for team in Team.select().where(Team.div == Divs):
        print(teamTemplate.format(team=team))
    # db.close()

def viewAllPlayers():
    print("All Players")
    print("-" * 35)

    for player in Player.select():
        print(playerTemplate.format(player=player))

#  Print Player Data
def positionbyTeam(teamName, postion):
    # db.connect()

    for team in Team.select().where(Team.name == teamName):
        print(teamTemplate.format(team=team))
    print("-" * 25)
    ################ Need custom order
    for player in Player.select().order_by(Player.overall.desc()).where((Player.teamName == teamName) & (Player.position == postion)):
        print(rosterTemplate.format(player=player))

    # db.close()

def playersbyTeam(teamName):
    # db.connect()

    for team in Team.select().where(Team.name == teamName):
        print(teamTemplate.format(team=team))
    print("-" * 25)
    ################ Need custom order
    # print each position by overall indiviually by team
    for player in Player.select().where(Player.teamName == teamName):
        for position in Player.select().order_by(Player.overall.desc()).where(Player.position == "QB"):
            print(playerTemplate.format(player=player))

    # db.close()

def getCurrentSeason():
    currentSeason = str(Season.select().order_by(Season.id.desc()).get().year)

    print("-------------- " + currentSeason + "-----------------")
    db.close()

playersbyTeam("Saints")