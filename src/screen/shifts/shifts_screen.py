from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from src.screen.shifts.utils.python.daily_shift import DailyShift
from src.screen.shifts.utils.python.call_info_popup import CallInfoPopup

class ShiftsScreen(Screen):
    offNum = ''
    callInfoPopup = None
    shiftsScreenRecycleView = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ShiftsScreen, self).__init__(**kwargs)
        self.callInfoPopup = CallInfoPopup()
    
    def setOffNum(self, offNum):
        self.offNum = offNum

    def showCallInfoPopup(self, driverInfoList):
        if self.callInfoPopup.populateCallInfo(driverInfoList):
            self.callInfoPopup.open()
        
    def servicesButton(self):
        self.manager.switchToServicesScreen()

    def logoutButton(self):
        self.manager.switchToLoginScreen()
