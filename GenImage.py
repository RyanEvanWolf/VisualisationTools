import numpy as np 
import sys
import os

import time

import VisualisationTools as vis



validConfig,ini=vis.readConfigFile("test.ini")
if(validConfig):
    try:
        plot=vis.createMapFromFile(ini)
        for i in range(0,10):
            print(i)
            sys.stdout.flush()
            plot[:]=i*np.ones(plot.shape,plot.dtype)[:]
            time.sleep(1)
    except Exception as e:
        print(e)
        raise RuntimeError("Unhandled Exception: Closing")
else:
    raise ValueError("Invalid Configuration File")


print("Program Halted Successfully")
sys.exit()
