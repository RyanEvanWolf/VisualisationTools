import ctypes
import struct
import configparser

import sys


import mmap


class struct_Playback(ctypes.Structure):
    _fields_ = [ ("RefreshRate_Hz",ctypes.c_uint8)]

    # def __init__(self,Rate_Hz=15,Paused=0):
    #     self.RefreshRate_Hz=Rate_Hz
    #     self.Pause=Paused


# class shr_Playback(struct_Playback):
#     def __init__(self,mmapDir="tmp/playback_map",Rate=0,Pause=0):
#         self.f=open(mmapDir,'w+')
#         self.map=mmap.mmap(self.f.fileno(),
#                         ct.sizeof(struct_Playback),
#                         access=mmap.ACCESS_WRITE)
#         self=ct.Structure.from_buffer(self.map,struct_Playback)
# class playBackManager:
#     def __init__(self,playback_dict):
#         self.settings=playBackSettings(0,0)
#         self.imageNumber=0

        
    