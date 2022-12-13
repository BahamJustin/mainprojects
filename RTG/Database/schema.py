from peewee import *

db = SqliteDatabase("league.db")

# Peewee video
# https://www.youtube.com/watch?v=Vk6Ptnvqr4M&ab_channel=IDGTECHtalk

# subclass
class BaseTable(Model):
    class Meta:
        database = db

#  Create Season
class Season(BaseTable):
    year = IntegerField(null=False, index=True)

# Create Divisions/Conferences
class Conference(BaseTable):
    name = CharField(null=False, index=True)

class Division(BaseTable):
    name = CharField(null=False, index=True)

# create team model
class Team(BaseTable):
    city = CharField(null=False, index=True)
    name = CharField(null=False, index=True)
    conf = ForeignKeyField(Conference, backref='teams')
    div = ForeignKeyField(Division, backref='teams')

    # teamID 

# Create actor base model
class Actor(BaseTable):
    firstName = CharField(null=False, index=True)
    lastName = CharField(null=False, index=True)
    # age
    #  team = ForeignKeyField(Team, backref='')

# Create Players
class Player(Actor):
    position = CharField(null=False, index=True)
    overall = IntegerField(null=False, index=True)
    teamName = ForeignKeyField(Team.name, backref='players')

# Create User 
class User(Actor):
    team = ForeignKeyField(Team, backref='user')