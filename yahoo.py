import os
import sys
import time
from audioplayer import AudioPlayer


APP_PATH = os.path.dirname(sys.executable)
if __file__:
    APP_PATH = os.path.dirname(__file__)
YAHOO = os.path.join(APP_PATH, 'yahoo.wav')
SOUND = AudioPlayer(YAHOO)

TIME = 0.2
GRANULARITY  = 0.01
REPEAT = 3
ALTERN = True

os.system("color 40")
os.system('mode con: cols=25 lines=10')

while 1:
    for repeat in range(REPEAT):
        SOUND.play()
        print("Yahoo!")
        time.sleep(TIME)
        print(TIME)
        if ALTERN:
            os.system("color 04")
            ALTERN = False
        else:
            os.system("color 40")
            ALTERN = True

    if (TIME-GRANULARITY) > 0.03:
        TIME -= GRANULARITY
