import numpy as np 
import sys
import os

import time

import VisualisationTools as vis
import Streaming          as visSt
import mmap


import ctypes

validConfig,ini=vis.readConfigFile("test.ini")
if(validConfig):
    try:
        settings=visSt.PlayBackSettings(ini["PlayBackSettings"])
        settings.setRefreshRate(30)
        imageMap=vis.createMapFromFile(ini)

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
