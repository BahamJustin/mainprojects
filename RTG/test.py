# from itertools import *
# from math import perm
# from turtle import home
# from Database.schema import *
# from Database.createData import *
# from Database.readData import *
# from peewee import *
import csv
import sys
import os
import random
import names

# teams = ["saints", "texans", "vikings"]
# players = ["John Smith", "Jim Baker", "Dusty Boot"]

def randomOverall():
    print(random.randrange(50, 99))

# for x in teams:
#   for y in range(5):
#     print(x, players[1])

# NameA = names.get_first_name()
# # NameB = names.get_last_name()

# firstNames = (['Justin', 'Jason'])
# lastNames = (['Baham', 'Baker'])

# randomFirstName = random.choice(firstNames)
# randomLastName = random.choice(lastNames)

for x in range(5) :
    print()

# nfcNorth = list(Team.select().where(Team.div == "NFC North"))
# nfcSouth = list(Team.select().where(Team.div == "NFC South"))
# nfcEast = list(Team.select().where(Team.div == "NFC East"))
# nfcWest = list(Team.select().where(Team.div == "NFC West"))
# afcNorth = list(Team.select().where(Team.div == "AFC North"))
# afcSouth = list(Team.select().where(Team.div == "AFC South"))
# afcEast = list(Team.select().where(Team.div == "AFC East"))
# afcWest = list(Team.select().where(Team.div == "AFC West"))




# comb = permutations(nfcNorth, 2)

# for i in list(comb):
#     homeName = Team.get_by_id(i[0]).name
#     awayName = Team.get_by_id(i[1]).name
#     print(homeName + " - " + awayName)
    

# def create_schedule(list):
#     """ Create a schedule for the teams in the list and return it"""
#     s = []

#     if len(list) % 2 == 0: list = list + ["BYE"]

#     for i in range(len(list)):

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

# print("Math-------")
# print(len(div1))
# print(4 % 2)
# print(range(len(div1)-1))
# print(int(len(div1) / 2))
# print(div1[:int(len(div1) / 2)])
# print(div1[int(len(div1) / 2):])
# print("-" * 35)

# def main():
#     for round in create_schedule(div1):
#         for match in round:
#             print(match[0] + " - " + match[1])
#     print
    # for round in create_schedule(div2):
    #     for match in round:
    #         print(match[0] + " - " + match[1])
    # print
    # for round in create_schedule(div3): 
    #     for match in round:
    #         print(match[0] + " - " + match[1])
    # print
    # for round in create_schedule(div1+div2+div3): 
    #     for match in round:
    #         print(match[0] + " - " + match[1])
    #     print

# if __name__ == "__main__":
#     main()

