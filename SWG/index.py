from main import *
from peewee import *
from pathlib import Path
from consolemenu import *
from consolemenu import SelectionMenu
from consolemenu.items import *
from Database.createData import *
from Database.readData import *
from Database.updateData import *
from Database.emergencyKill import killDatabase
from playhouse.shortcuts import *
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.properties import StringProperty, ListProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader

Window.size = (414, 736)

class WindowManager(ScreenManager):
    pass

wm = WindowManager()
app= App.get_running_app()

class EquipmentScreen(Screen):
    ### Be able to equip items to different equipment slots - equipment affects stats
    pass

class ItemDesc(Screen):
    instance = None
    itemDescName = StringProperty()
    itemDescType = StringProperty()
    itemDescSkill = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ItemDesc.instance = self

    def viewItem(self, name):
        focusItem = PlayerInventory.get(PlayerInventory.name == name)
        self.itemDescName = focusItem.name
        self.itemDescType = focusItem.itemType
        self.itemDescSkill = focusItem.bonusSkill
        print(name)

class WeaponStack(StackLayout):
    ### Click Item to see Item Description Screen
    instance = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        WeaponStack.instance = self

    ### How to change screens from python file?
    # def viewScreen(self):
    #     try:
    #         wm.current = "ids"
    #         print("it works?")
    #     except:
    #         print("FUCK")

    def viewWeapons(self):
        self.clear_widgets()
        for i in PlayerInventory.select().where(PlayerInventory.itemType == "Weapon"):
            size = dp(100)
            dictItem = model_to_dict(i) 
            # print(dictItem['name'])
            invButton = Button(text=dictItem['name'], size_hint=(None, None), size=(size, size))
            self.add_widget(invButton)
            invButton.bind(on_release=lambda x:ItemDesc.instance.viewItem(invButton.text))
            # READ NAME OF EACH INDIVIDUAL BUTTON
            # print name with widget.text??
            # invButton.bind(on_press=lambda x:self.viewScreen())
        # print("-" * 35)

class MiscStack(StackLayout):
    instance = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        MiscStack.instance = self

    def viewMisc(self):
        self.clear_widgets()
        for i in PlayerInventory.select().where(PlayerInventory.itemType == "Misc"):
            size = dp(100)
            dictItem = model_to_dict(i) 
            # print(dictItem['name'])
            invButton = Button(text=dictItem['name'], size_hint=(None, None), size=(size, size))
            self.add_widget(invButton)
            invButton.bind(on_release=lambda x:ItemDesc.instance.viewItem(dictItem['name']))
        # print("-" * 35)

    ### Try to combine all stacks using an id to call specific categories 
    # def viewMisc(self, category):
    #     self.clear_widgets()
    #     for i in PlayerInventory.select().where(PlayerInventory.itemType == category):
    #         size = dp(100)
    #         dictItem = model_to_dict(i) 
    #         # print(dictItem['name'])
    #         invButton = Button(text=dictItem['name'], size_hint=(None, None), size=(size, size))
    #         self.add_widget(invButton)

class InvTabs(TabbedPanel):
    pass

class InventoryScreen(Screen):
    def updateInv(self, *largs):
        WeaponStack.instance.viewWeapons()
        MiscStack.instance.viewMisc()    

class SkillScreen(Screen):
    skillInfo = StringProperty()

    def getSkillInfo(self, *largs):
        if User.get().forceSensitivity == 1:
            playerForceSense = "Yes"
        else:
            playerForceSense = "No"

        self.skillInfo = f"""
        Force Sensitivty: {playerForceSense}
        Force Skill: {User.get().forceSkill}
        Melee: {User.get().meleeSkill}
        Ranged: {User.get().rangedSkill}
        Agility: {User.get().agilitySkill}
        Piloting: {User.get().pilotingSkill}
        Stealth: {User.get().stealthSkill}
        Trade: {User.get().tradeSkill}
        Smuggling: {User.get().smugglingSkill}
        Leadership: {User.get().leadershipSkill}
        Strategy: {User.get().strategySkill}
        Medical: {User.get().medicalSkill}
        Tracking: {User.get().trackingSkill}
        Slicing: {User.get().slicingSkill}
        Engineering: {User.get().engineeringSkill}"""

class CharacterMenu(Screen):
    playerInfo = StringProperty()

    def getCharacterInfo(self, *largs):
        self.playerInfo = f"""
        Name: {User.get().name} {User.get().familyName} 
        Age: {User.get().age}                     
        Race: {User.get().race}
        Home Planet: {User.get().homePlanet}"""


class RelationshipMenu(Screen):
    ### Display actors - Family, Friends, Rivals, By relation, By Planet, etc.
    ### Companions - Rivals
    ### First need to assign relations, design relation score, companion systems
    pass

class ActionMenu(Screen):
    ### Training, Jobs, 
    pass

class PlanetMenu(Screen):
    ### View Inhabitants, Visit other settlements, visit settlement locations
    pass
        
class DevTestMenu(Screen):
    def devAdvanceTime(self):
        advanceTime()
    
    def addInventory(self):
        randItems()

class EventScreen(Screen):
    ### See new events happen, View Event History
    ### Current Galactic CLimate Screens? - current tensions, attacks, news, factions
    ### 
    pass

class CreateUserMenu(Screen):
    ### Can only enter first name currently
    userName = StringProperty("UserName")
    familyName = StringProperty("FamName")
    userRace = StringProperty("Race")
    userHome = StringProperty("Home Planet")

    def on_text_validate(self, widget):
        ### clear text box
        self.userName = widget.text
        newUser(self.userName, self.familyName, self.userRace, self.userHome)

class NewGameMenu(Screen):
    def startNewGame(self):
        newGame()

class MainMenu(Screen):
    ### Display current planet Info etc.
    try:
        gameDate = StringProperty(getDate())
        userName = StringProperty(User.get().name)
    except:
        gameDate = StringProperty("No DB")
        userName = StringProperty("No DB")

    def getMainInfo(self, *largs):
        try:
            self.gameDate = getDate()
            self.userName = User.get().name
        except:
            pass
        # pg_db.close()

class TitleWindow(Screen):
    ### Progress bar on botttom, lore skyrim style on top of progress bar, load icon in middle, when done, pull up main window
    try:
        userName = StringProperty(User.get().name)
        userExists = True
    except:
        userName = "No Game"
        userExists = False

    def getTitleInfo(self, *largs):
        try:
            self.userName = User.get().name
            self.userExists = True
        except:
            pass

    def killDB(self):
        killDatabase()

wm.add_widget(ItemDesc(name="ids"))

class SWGApp(App):
    pass

if __name__ == "__main__":
    SWGApp().run()