#!/usr/bin/env python3

# from omxplayer.player import OMXPlayer
# from pathlib import Path
# from time import sleep

# VIDEO_PATH = Path("./media/test1.mp4")

#player = OMXPlayer(VIDEO_PATH)
# vid = OMXPlayer('./media/test1.mp4',args=['--loop'])

#vid.play()

# sleep(5)
# vid.quit()

#player.quit()


import sys
print (sys.version_info)

movie_path = '../media/test2.mp4'

from subprocess import Popen

omxp = Popen(['omxplayer', '-o', 'local', '--loop', '--no-osd' ,movie_path])