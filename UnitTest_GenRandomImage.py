import numpy as np 
import sys
import os

import time

import mmap


import VisualisationTools.Streaming.Settings as playSet
import VisualisationTools.Streaming.PlayBack as play


import ctypes

validConfig,ini=playSet.readConfigFile("VisualisationTools/test.ini")
if(validConfig):
    try:
        settings=play.PlayBackSettings(ini["PlayBackSettings"],
                                        "VisualisationTools/tmp/playback.mmap")
        settings.setRefreshRate(30)
        imageMap=play.createMapFromFile(ini)

        onesImage=np.random.rand(imageMap.shape[0],imageMap.shape[1])
        for i in range(0,20*10):
            imageMap[:]=i*25*onesImage
            settings.setFrameNumber(i)
            time.sleep(1/10)
    except Exception as e:
        print(e)
        raise RuntimeError("Unhandled Exception: Closing")
else:
    raise ValueError("Invalid Configuration File")


print("Program Halted Successfully")
sys.exit()
