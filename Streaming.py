import ctypes
import mmap


import configparser

import sys


import mmap


class struct_Playback(ctypes.Structure):
    _fields_ = [ ("RefreshRate_Hz",ctypes.c_uint8),
                 ("Paused",ctypes.c_uint8),
                 ("Kill",ctypes.c_uint8),
                 ("FrameNumber",ctypes.c_uint64)]
    def __repr__(self):
        return "{0},{1}".format(self.RefreshRate_Hz,
                                self.FrameNumber)


class PlayBackSettings():
    def __init__(self,configIni=None,mapFile="tmp/playback.mmap"):
        if(configIni==None):
            fPermission='r'
            mapPermission=mmap.ACCESS_READ
        else:
            fPermission='r+'
            mapPermission=mmap.ACCESS_WRITE
        self.f=open(mapFile,fPermission)
        self.map=mmap.mmap(self.f.fileno(),
                        ctypes.sizeof(struct_Playback),
                        access=mapPermission)  
        self.ptr_settings=ctypes.POINTER(struct_Playback)
        mmapAddress=ctypes.addressof(ctypes.c_uint8.from_buffer(self.map))
        self.ptr_settings=ctypes.cast(mmapAddress,self.ptr_settings)
    def setRefreshRate(self,Rate):
        self.ptr_settings.contents.RefreshRate_Hz=ctypes.c_uint8(Rate)          
    def setFrameNumber(self,number):
        self.ptr_settings.contents.FrameNumber=ctypes.c_uint64(number)

        
    