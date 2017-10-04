#!/usr/bin/env python3

from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

VIDEO_PATH = Path("./media/test1.mp4")

#player = OMXPlayer(VIDEO_PATH)
vid = OMXPlayer('./media/test1.mp4',args=['--loop'])

#vid.play()

sleep(5)
vid.quit()

#player.quit()