from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty
from kivy.properties import StringProperty

from src.data.admin.collect.data_collector import DataCollector
from src.screen.login.utils.update_popup import UpdatePopup

from src.data.read.read_services import readServices
from src.data.read.read_shifts import readShifts
from src.data.admin.repair.repair_all_files import repairAllFiles
from src.data.admin.repair.update_backup_dir import updateBackupDir
from src.screen.login.utils.get_warning_message_info import (
    getWarningMessageInfo
    )
from src.screen.login.utils.update_popup_util import showPopup
from src.data.user.update_required_date_check import (
    updateRequiredDateCheck
    )
from src.data.user.download_data_from_dropbox import (
    downloadDataFromDropbox
    )

class LoginScreen(Screen):
    ADMIN = False
    offNumTextInput = ObjectProperty(None) # object in kv
    warningMessage = StringProperty() # binding
    warningMessageColor = tuple() # binding
    updateDone = BooleanProperty(False)
    updatePopup = None
    
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.updatePopup = UpdatePopup()
        self.setWarningMessage()
        if not self.ADMIN and updateRequiredDateCheck():
            downloadDataFromDropbox()

    def setWarningMessage(self):
        warningMessageInfo = getWarningMessageInfo()
        self.warningMessage = warningMessageInfo['message']
        self.warningMessageColor = warningMessageInfo['color']

    def loginButton(self):
        offNum = self.offNumTextInput.text
        servicesData = readServices(offNum)
        shiftsData = readShifts(offNum)
        if servicesData and shiftsData:
            self.manager.updateScreens(offNum, servicesData, shiftsData)
            self.manager.switchToServicesScreen()
        else:
            self.manager.loginFailure()

    @showPopup
    def updateButton(self):
        dataCollector = DataCollector()
        finished = False
        updateResult = dict()
        while not finished:
            updateResult = dataCollector.keepCollectingData()
            finished = updateResult['finished']
            self.updatePopup.text = updateResult['message']
   
        self.updatePopup.dotsTimer.cancel()
        success = updateResult['success']
        error = updateResult['error']
        if success:
            updateBackupDir()
            self.setWarningMessage()
            self.updatePopup.text = 'Azurirano!'
        elif error:
            repairAllFiles()
            self.updatePopup.text = 'GRESKA! Dokumenti popravljeni.'
        else:
            self.updatePopup.text = 'Sluzbe jos nisu izasle!'

        self.updatePopup.auto_dismiss = True

