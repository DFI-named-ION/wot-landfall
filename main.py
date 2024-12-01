import BigWorld
from gui import SystemMessages

def _loop():
    SystemMessages.pushMessage('Hello!1!', type=SystemMessages.SM_TYPE.Warning)
    BigWorld.callback(2, _loop)

_loop()