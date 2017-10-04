#!/usr/bin/env python3

# from omxplayer import OMXPlayer
#from pathlib import Path
# from time import sleep

# VIDEO_PATH = Path("./media/test1.mp4")

#player = OMXPlayer(VIDEO_PATH)
# player = OMXPlayer('../media/test2.mp4', args=['-o', 'local', '--loop', '--no-osd'])
# player.play()
#vid.play()

# sleep(5)
# vid.quit()

#player.quit()


# import sys
# print (sys.version_info)

# movie_path = '../media/test2.mp4'

from subprocess import Popen

# omxp = Popen(['omxplayer', '-o', 'local', '--loop', '--no-osd' , '../media/test2.mp4'])

omxp = Popen(['omxplayer', '-o', 'local', '--loop', '--no-osd' , '../media/test1.mp4'])