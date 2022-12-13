import os
from os import *
import random
import names
import psycopg2
import json
from consolemenu import *
from consolemenu.items import *
from Database.schema import *
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

allSkills = {
    "MeleeIII": {
    "skillName": "MeleeIII",
    "skillType": "meleeSkill",
    "skillBonus": 3
    },
    "TradeV": {
        "skillName": "TradeV",
        "skillType": "tradeSkill",
        "skillBonus": 5
    },
    "SlicingDebuffII": {
        "skillName": "SlicingDebuffII",
        "skillType": "slicingSkill",
        "skillBonus": -2
    },
    # "NoSkill": {
    #     "skillType": null,
    #     "skillBonus": null
    # }
}

equipment = ("Body Pillow", "Misc", "TradeV")    

def randSkill():
    return random.choice(list(allSkills))

def skillShit():
    user = User.get_by_id(1)

    # find skill on item
    itemSkill = equipment[2]
    print("Item Skill: ",itemSkill)

    # find item skill type
    itemSkillType = allSkills[itemSkill].get("skillType")
    print("Item Skill Type: ",itemSkillType)

    # find skill bonus of skill on item
    itemSkillBonus = allSkills[itemSkill].get("skillBonus")
    print("Item Skill Bonus: ",itemSkillBonus)

    if itemSkillType == "tradeSkill":
        # find skill of user
        print("User Skill: ",user.tradeSkill)

        # add skill bonus to user skill and update user skill
        afterBonus = user.tradeSkill + itemSkillBonus
        user.tradeSkill = afterBonus
        user.save()
        print("New Skill Value: ", user.tradeSkill)
    else:
        pass

# skillShit()

# def skillShit():
#     user = User.get_by_id(1)

#     # find skill on item
#     itemSkill = equipment[2]
#     print("Item Skill: ",itemSkill)

#     # find item skill type
#     itemSkillType = allSkills[itemSkill].get("skillType")
#     print("Item Skill Type: ",itemSkillType)

#     # find skill bonus of skill on item
#     itemSkillBonus = allSkills[itemSkill].get("skillBonus")
#     print("Item Skill Bonus: ",itemSkillBonus)

#     # # Find player base skill
#     # baseSkill = findValue(itemSkillType)
#     # print(f"Base Player {itemSkillType}: {baseSkill}")

#     # # find new skill value
#     # baseSkill = baseSkill + itemSkillBonus

#     # updateValue(itemSkillType, baseSkill)

#     # baseSkill = getattr(user, itemSkillType)

#     # 
#     # Cant reference the user.skill with variable/parameter to update value 
#     # 

#     # try:
#     #     print(f"User Skill: {baseSkill}")
#     #     # add skill bonus to user skill and update user skill
#     #     baseSkill = baseSkill + itemSkillBonus
#     #     # find new way to save it to user
#     #     user.save()
#     #     print(f"New Skill Value: {getattr(user, itemSkillType)}")
#     # except:
#     #     pass

#     # if itemSkillType == "tradeSkill":
#     #     # find skill of user
#     #     print("User Skill: ",user.tradeSkill)

#     #     # add skill bonus to user skill and update user skill
#     #     afterBonus = user.tradeSkill + itemSkillBonus
#     #     user.tradeSkill = afterBonus
#     #     user.save()
#     #     print("New Skill Value: ", user.tradeSkill)
#     # else:
#     #     pass

# 
# <class 'OSError'> - 
# 

# def findValue(skillType):
#     user = User.get_by_id(1)
#     return getattr(user, str(skillType), None)

# def updateValue(
#     # itemSkillType, 
#     # baseSkill
#     ):

#     playerTrade = "tradeSkill"

#     # update user
#     # sql = f"""SELECT * FROM User;"""

#     sql = """
#     SELECT * FROM User
#     """

#     try:
#         conn = psycopg2.connect(host='localhost', user='postgres', password='Saints504!')
#         cur = conn.cursor()

#         # conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#         # cur.execute(sql, (itemSkillType, baseSkill))
#         cur.execute(sql)

#         conn.commit()
#         cur.close()
#     except:
#         print(error)

# 
# example issu
# 

# Owner, by default, owns 1 home, 2 boats, and 3 cars
# class Owner(BaseTable):
#     homes = IntegerField(null=False, default = 1)
#     boats = IntegerField(null=False, default = 2)
#     cars = IntegerField(null=False, default = 3)

# owner = Owner.get_by_id(1)

# allAssets = {
#     "House1": {
#         "assetType": "homes"
#     },
#     "Boat1": {
#         "assetType": "boats"
#     }
# }

# # returns 'homes'
# House1Type = allAssets["House1"].get("assetType")

# # returns 1
# print(owner.homes)

# AttributeError: 'Owner' object has no attribute 'assetType'
# def findValue(assetType):
#     print(owner.assetType)

# # GOAL: return '1'
# findValue(House1Type)

# # if house 1 is type 'boats', show owner.boats value
# # if house 1 is type 'homes', show owner.homes value
# if House1Type == "boats":
#     print("Owned Boats: ",owner.boats)
# elif House1Type == "homes":
#     print("Owned Homes: ",owner.homes)
# else:
#     pass