from kivy.uix.boxlayout import BoxLayout

class DailyShift(BoxLayout):
    def callInfoButton(self, driverInfo):
        parent = self.parent
        # workaround
        while not (hasattr(parent, 'showCallInfoPopup') and
                   callable(getattr(parent, 'showCallInfoPopup'))): 
            parent = parent.parent
        parent.showCallInfoPopup(driverInfo)
        
