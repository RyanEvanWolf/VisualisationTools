import numpy as np 
import sys
import os

import time
from matplotlib.pyplot import figure, draw, pause, get_cmap

import collections
from statistics import mean


import VisualisationTools.Streaming.Settings as playSet
import VisualisationTools.Streaming.PlayBack as play


validConfig,ini=playSet.readConfigFile("VisualisationTools/test.ini")
if(validConfig):
    try:
        settings=play.PlayBackSettings(ini["PlayBackSettings"],
                                        "VisualisationTools/tmp/playback.mmap")
        delay=1/settings.getRefreshRate()
        print("Expected Update Rate",delay,1/delay)

        sys.stdout.flush()

        fg = figure()
        ax = fg.gca()
        font = {'family': 'serif',
            'color':  'red',
            'weight': 'normal',
            'size': 8,
            }
       
        fps_text=ax.text(0,-12,"FPS :0",font)
        time_text=ax.text(0,-24,"Time:0",font)
        frame_text=ax.text(0,-36,"Fno :0",font)
        update_text=ax.text(0,-48,"Frame Delta :0",font)

        baseImage=play.readMapFromFile(ini)
        h=ax.imshow(baseImage,cmap='jet',vmin=0,vmax=255)
        fg.colorbar(h,orientation='vertical')


        fg.show()
        updateQ=collections.deque([delay] * 5, maxlen=5)
        frameQ=collections.deque([0] * 5,maxlen=5)
        
        most_recent_time=time.process_time()
        previousSeenFrame=0
        while(True):
            newStamp=time.process_time()
            newframe=settings.getFrameNumber()

            updateQ.append((newStamp-most_recent_time)*2)
            frameQ.append(newframe-previousSeenFrame)

            avgFrames=mean(frameQ)
            avgUpdate=mean(updateQ)
            
            most_recent_time=newStamp
            previousSeenFrame=newframe
            
            try:
                fps_text.set_text("FPS :{0:2.1f}".format(1/avgUpdate))
                time_text.set_text("Time:{0:.1f}".format(most_recent_time))
                frame_text.set_text("Fno :{0}".format(previousSeenFrame))
                update_text.set_text("Frame Delta :{0:.1f}".format(frameQ[-1]))
            except:
                print("e")

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
