import numpy as np 
import sys
import os

import time

import VisualisationTools as vis
import Streaming          as visSt


from matplotlib.pyplot import figure, draw, pause, get_cmap

validConfig,ini=vis.readConfigFile("test.ini")
if(validConfig):
    try:
        settings=visSt.PlayBackSettings(ini["PlayBackSettings"])
        delay=1/settings.getRefreshRate()
        print(delay)

        fg = figure()
        ax = fg.gca()

        baseImage=vis.readMapFromFile(ini)
        h=ax.imshow(baseImage,cmap='seismic',vmin=0,vmax=255)#,get_cmap('gray'))
        fg.colorbar(h,orientation='vertical')

        font = {'family': 'serif',
                'color':  'red',
                'weight': 'normal',
                'size': 16,
                }

        fg.show()
        while(True):
            h.set_data(baseImage)
            draw()
            fg.canvas.flush_events()
            time.sleep(delay)

    except Exception as e:
        print(e)
        raise RuntimeError("Unhandled Exception: Closing")
else:
    raise ValueError("Invalid Configuration File")


print("Program Halted Successfully")
sys.exit()
