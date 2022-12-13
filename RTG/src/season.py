from ..Database.schema import *
from ..Database.createData import *
from ..Database.readData import *
from peewee import *
import csv
import sys
import os
import random

# Create an 18 week Season


#  /////////////////////////////////////////////////////////////////////////////////

# def createWeek():
#     class homeTeam:
#         anyTeam = Team.select().order_by(fn.Random()).limit(1).get() 
#         name = anyTeam.name
#         city = anyTeam.city
    
#     class awayTeam:
#         anyTeam = Team.select().order_by(fn.Random()).limit(1).get() 
#         name = anyTeam.name
#         city = anyTeam.city
    
#     if homeTeam.name == awayTeam.name:
#         createWeek()
#     else:
#         print("Week 1: " + "The " + homeTeam.city + " " + homeTeam.name + " Vs. The " + awayTeam.city + " " +  awayTeam.name)
#     db.close()

# def createSeason():
#     print(random.shuffle(teams))

# createSeason()
# ////////////////////////////////////////////////////////////////////////////////////////////////////////

# nfcNorth = list(Team.select().where(Team.div == "NFC North"))
# nfcSouth = list(Team.select().where(Team.div == "NFC South"))
# nfcEast = list(Team.select().where(Team.div == "NFC East"))
# nfcWest = list(Team.select().where(Team.div == "NFC West"))
# afcNorth = list(Team.select().where(Team.div == "AFC North"))
# afcSouth = list(Team.select().where(Team.div == "AFC South"))
# afcEast = list(Team.select().where(Team.div == "AFC East"))
# afcWest = list(Team.select().where(Team.div == "AFC West"))

# def create_schedule(list):
    # """ Create a schedule for the teams in the list and return it"""
#     s = []

#     if len(list) % 3 == 1: list = list + ["BYE"]

#     for i in range(len(list)-1):

#         mid = int(len(list) / 2)
#         l1 = list[:mid]
#         l2 = list[mid:]
#         l2.reverse()    

#         # Switch sides after each round
#         if(i % 2 == 1):
#             s = s + [ zip(l1, l2) ]
#         else:
#             s = s + [ zip(l2, l1) ]

#         list.insert(1, list.pop())

#     return s

# print(4 % 3)
# print(len(nfcNorth))

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def main():
#     nfcConf = nfcEast+nfcNorth+nfcSouth+nfcWest
#     afcConf = afcEast+afcNorth+afcSouth+afcWest

#     for round in create_schedule(nfcNorth):
#         for match in round:
#             homeName = Team.get_by_id(match[0]).name
#             awayName = Team.get_by_id(match[1]).name
#             print(homeName + " - " + awayName)
#     print
    # for round in create_schedule(nfcSouth):
    #     for match in round:
    #         homeName = Team.get_by_id(match[0]).name
    #         awayName = Team.get_by_id(match[1]).name
    #         print(homeName + " - " + awayName)
    # print
    # for round in create_schedule(nfcEast): 
    #     for match in round:
    #         homeName = Team.get_by_id(match[0]).name
    #         awayName = Team.get_by_id(match[1]).name
    #         print(homeName + " - " + awayName)
    # print
    # for round in create_schedule(nfcWest): 
    #     for match in round:
    #         homeName = Team.get_by_id(match[0]).name
    #         awayName = Team.get_by_id(match[1]).name
    #         print(homeName + " - " + awayName)
    # print
    # for round in create_schedule(afcNorth):
    #     for match in round:
    #         homeName = Team.get_by_id(match[0]).name
    #         awayName = Team.get_by_id(match[1]).name
    #         print(homeName + " - " + awayName)
    # print
    # for round in create_schedule(afcSouth):
    #     for match in round:
    #         homeName = Team.get_by_id(match[0]).name
    #         awayName = Team.get_by_id(match[1]).name
    #         print(homeName + " - " + awayName)
    # print
    # for round in create_schedule(afcEast): 
    #     for match in round:
    #         homeName = Team.get_by_id(match[0]).name
    #         awayName = Team.get_by_id(match[1]).name
    #         print(homeName + " - " + awayName)
    # print
    # for round in create_schedule(afcWest): 
    #     for match in round:
    #         homeName = Team.get_by_id(match[0]).name
    #         awayName = Team.get_by_id(match[1]).name
    #         print(homeName + " - " + awayName)
    # print
    # for round in create_schedule(nfcConf): 
    #     for match in round:
    #         print(homeName + " - " + awayName)
    # print

# main()

# ////////////////////////////////////////////////////////////////////////////////////////////

# def GenerateFixtures(self):
#     #  ????
#     ghostteam = 0

#     # 
#     teams = self.teams

#     # checking if theres 2 teams?
#     if self.teams % 2 == 1:
#         ghostteam = 1
#         teams = teams + 1
    
#     # games in a season?
#     totalRounds = teams - 1

#     # games per week
#     matches = int((teams) / 2)
#     self.finishweek = (totalRounds * self.rounds) + self.startweek

#     # ?????
#     if self.finishweek == 0:
#         self.finishweek = -1

#     # 
#     iterations = self.rounds

#     # 
#     home = 0
#     away = 0
#     swop = 0
#     counter = 0
#     LeagueTeamList = []

#     # 
#     if ghostteam == 1:
#         LeagueTeamList.append(-1)

#     # 
#     for t in TeamList:
#         if t.league == self:
#             LeagueTeamList.append(t.id)

#     # for each week in the season...
#     for r in range(0,totalRounds):
#         # foir each game in a week...
#         for m in range (0, matches):
#             # 
#             home = (r + m) % (teams - 1)
#             away = (teams - 1 - m + r) % (teams - 1)

#             if m == 0:
#                 away = (teams - 1)
#             if r % 2 == 1:
#                 swop = home
#                 home = away
#                 away = swop

#             for i in range(0, iterations):
#                 if i % 2 == 0:
#                     f = Fixture([(totalRounds*i)+r+self.startweek,LeagueTeamList[home-1],LeagueTeamList[away-1],1,self])
#                 else:
#                     f = Fixture([(totalRounds*i)+r+self.startweek,LeagueTeamList[away-1],LeagueTeamList[home-1],1,self])