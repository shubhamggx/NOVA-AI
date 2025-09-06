import os
import eel
import time
from engine.features import *
from engine.command import *

eel.init('www')



# Start the app without playing sound yet
os.system('start msedge --app="http://localhost:8080/index.html"')



playAssistantSound()
# Start eel
eel.start('index.html', port=8080, mode=None, host='localhost', block=True)
# hl0 hlo
