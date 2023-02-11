from kivy.uix.popup import Popup
from kivy.core.clipboard import Clipboard
from kivy.properties import StringProperty

from jnius import autoclass
from jnius import cast

class CallInfoPopup(Popup):
    name = StringProperty() # binding
    phoneNumber = StringProperty() # binding

    def __init__(self, **kwargs):
        super(CallInfoPopup, self).__init__(**kwargs)

    def populateCallInfo(self, driverInfo):
        # expected: driverInfo = [name] [surname] \n [phoneNumber]
        if('\n' not in driverInfo):
            return False
        driverInfoList = driverInfo.split('\n')
        self.name = driverInfoList[0]
        self.phoneNumber = driverInfoList[1]
        return True

    def copyNameOnClipboard(self):
        Clipboard.copy(self.name)

    def copyPhoneNumberOnClipboard(self):
        Clipboard.copy(self.phoneNumber)
            
    def callNumber(self):
        Intent = autoclass('android.content.Intent')        
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Uri = autoclass('android.net.Uri')
        intent = Intent(Intent.ACTION_DIAL)         
        intent.setData(Uri.parse("tel:" + self.phoneNumber))     
        currentActivity = cast('android.app.Activity',
                               PythonActivity.mActivity)                                                   
        currentActivity.startActivity(intent)

    def saveContact(self):      
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Contact = autoclass('org.test.Contact') # buildozer.spec
        currentActivity = cast('android.app.Activity',
                               PythonActivity.mActivity)
        Contact.addContact(currentActivity, self.name.title(),
                           self.phoneNumber.title())
    
