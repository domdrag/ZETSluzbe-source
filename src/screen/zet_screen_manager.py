import os

from kivy.uix.screenmanager import ScreenManager

from src.screen.login.login_screen import LoginScreen
from src.screen.services.services_screen import ServicesScreen
from src.screen.shifts.shifts_screen import ShiftsScreen

# workaround; portrait orientation not working for some reason [?]; 
os.environ['KIVY_ORIENTATION'] = "Portrait" 

class ZETScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(ZETScreenManager, self).__init__(**kwargs)
        #self.current = 'loginScreen'

    def loginFailure(self):
        self.loginScreen.updatePopup.text = 'Greska kod dohvacanja sluzbi.'
        self.loginScreen.updatePopup.open()
            
    def updateScreens(self, offNum, servicesData, shiftsData):
        self.servicesScreen.setOffNum(offNum)
        self.shiftsScreen.setOffNum(offNum)
        self.servicesScreen.servicesScreenRecycleView.data = servicesData
        self.shiftsScreen.shiftsScreenRecycleView.data = shiftsData

    def switchToServicesScreen(self):
        if self.current == 'loginScreen':
            self.transition.direction = 'down'
        else:
            self.transition.direction = 'right'
        self.current = 'servicesScreen'

    def switchToShiftsScreen(self):
        self.transition.direction = 'left'
        self.current = 'shiftsScreen'

    def switchToLoginScreen(self):
        self.transition.direction = 'up'
        self.current = 'loginScreen'
