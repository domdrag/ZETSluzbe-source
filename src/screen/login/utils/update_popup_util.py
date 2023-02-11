import threading

from src.screen.login.utils.dots_timer import DotsTimer

def addDots(updatePopup):
    if('...' in updatePopup.text):
        updatePopup.text = updatePopup.text[:-3]
    else:
        updatePopup.text = updatePopup.text + '.'
            

def showPopup(function):
    def wrap(loginScreen, *args, **kwargs):
        loginScreen.updatePopup.auto_dismiss = False
        loginScreen.updateDone = False  
        loginScreen.bind(updateDone = loginScreen.updatePopup.dismiss)  
        loginScreen.updatePopup.open()
        thread = threading.Thread(target=function,
                                  args = [loginScreen,
                                          *args],
                                  kwargs=kwargs)  
        loginScreen.updatePopup.dotsTimer = \
                DotsTimer(0.5, lambda: addDots(loginScreen.updatePopup))
        loginScreen.updatePopup.dotsTimer.start()
        thread.start() 
        return thread

    return wrap
