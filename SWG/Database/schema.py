from peewee import *
from playhouse.postgres_ext import *
from playhouse.postgres_ext import PostgresqlExtDatabase
from psycopg2.extensions import ISOLATION_LEVEL_SERIALIZABLE

pg_db = PostgresqlExtDatabase("galaxy", port=5432, user='postgres', password="Saints504!", isolation_level=ISOLATION_LEVEL_SERIALIZABLE)

class BaseTable(Model):
    name = CharField(null=False, index=True)

    class Meta:
        database = pg_db

class Settlement(BaseTable):
    homePlanet = CharField(null=False, index=True)

class Item(BaseTable):
    itemType = CharField(null=False, index=True)
    bonusSkill = CharField(null=True, index=True)

    # bonusTrait = CharField(null=True, index=True)

class Faction(BaseTable):
    pass

class Event(BaseTable):
    pass

class Actor(BaseTable):
    familyName = CharField(null=False, index=True)
    race = CharField(null=False, index=True)
    age = IntegerField(null=False, index=True)
    homePlanet = CharField(null=False, index=True)
    # profession = CharField(null=False, index=True)
    # forceSensitivity = BooleanField(null=False, index=True)
    # forceSkill = IntegerField(null=False, index=True)
    meleeSkill = IntegerField(null=False, index=True)
    rangedSkill = IntegerField(null=False, index=True)
    agilitySkill = IntegerField(null=False, index=True)
    pilotingSkill = IntegerField(null=False, index=True)
    stealthSkill = IntegerField(null=False, index=True)
    tradeSkill = IntegerField(null=False, index=True)
    # smuggling = crime check
    smugglingSkill = IntegerField(null=False, index=True)
    leadershipSkill = IntegerField(null=False, index=True)
    strategySkill = IntegerField(null=False, index=True)
    medicalSkill = IntegerField(null=False, index=True)
    trackingSkill = IntegerField(null=False, index=True)
    survivalSkill = IntegerField(null=False, index=True)
    trappingSkill = IntegerField(null=False, index=True)
    slicingSkill = IntegerField(null=False, index=True)
    engineeringSkill = IntegerField(null=False, index=True)

    # no crafting skill - instead recipe/skill locked
    # craftingSkill = IntegerField(null=False, index=True)
    
    # traits = ArrayField(null=False, index=True)
    # languages = ArrayField(null=False, index=True)
    # companions = ArrayField(null=False, index=True)
    
class Planet(BaseTable):
    actors = ForeignKeyField(Actor, backref='Home Planet', null=True)
    settlements = ForeignKeyField(Settlement, backref='Planet', null=True)
    pass

class User(Actor):
    id = IntegerField(null=False, default=1, unique=True)
    forceSensitivity = BooleanField(null=False, index=True)
    forceSkill = IntegerField(null=False, index=True)
    pass

class PlayerInventory(Item):
    pass

class Companion(Actor):
    pass

class Date(Model):
    id = IntegerField(null=False, default=1, unique=True)
    month = IntegerField(null=False, index=True, default=1)
    year = IntegerField(null=False, index=True, default=4)

    class Meta:
        database = pg_db