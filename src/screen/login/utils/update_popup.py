from kivy.uix.popup import Popup
from kivy.properties import StringProperty

class UpdatePopup(Popup):
    text = StringProperty() # binding
    dotsTimer = None
    
    def __init__(self, **kwargs):
        super(UpdatePopup, self).__init__(**kwargs)
