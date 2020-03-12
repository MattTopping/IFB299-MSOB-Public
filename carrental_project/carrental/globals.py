# Global variables

USER_LOGGEDIN = False

def changeLoginState(state):
    USER_LOGGEDIN = state

def returnLoginState():
    return USER_LOGGEDIN
