from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from src.screen.services.utils.daily_service import DailyService

class ServicesScreen(Screen):
    offNum = ''
    servicesScreenRecycleView = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ServicesScreen, self).__init__(**kwargs)
    
    def setOffNum(self, offNum):
        self.offNum = offNum

    def shiftsButton(self):
        self.manager.switchToShiftsScreen()
        
    def logoutButton(self):
        self.manager.switchToLoginScreen()
