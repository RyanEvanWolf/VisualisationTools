import numpy as np 
import sys
import os

import time

import VisualisationTools as vis



validConfig,ini=vis.readConfigFile("test.ini")
if(validConfig):
    try:
        plot=vis.readMapFromFile(ini)
        print(plot)
    except Exception as e:
        print(e)
        raise RuntimeError("Unhandled Exception: Closing")
else:
    raise ValueError("Invalid Configuration File")


print("Program Halted Successfully")
sys.exit()
