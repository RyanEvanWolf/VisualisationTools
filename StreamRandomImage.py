import numpy as np 
import sys
import os

import time

import VisualisationTools as vis
import Streaming          as visSt
import mmap


import ctypes




# ptr_pb=ctypes.POINTER(visSt.struct_Playback)

# obj=visSt.struct_Playback(0x22)

# test=ctypes.addressof(obj)

# print("0x{:X}".format(test))


# ptr_pb=ctypes.cast(test,ptr_pb)
# #


# print(ptr_pb)

# ptr_pb.contents.RefreshRate_Hz=155

# print(obj)




# ptr_settings=ctypes.POINTER(visSt.struct_Playback)

# f=open("tmp/playback_map",'r+')
# m=mmap.mmap(f.fileno(),
#                 2,
#                 access=mmap.ACCESS_WRITE)

# m.write(b"wa")

# print(ptr_settings)
# mmap_ptr=ctypes.addressof((ctypes.c_uint8*2).from_buffer(m))

# ptr_settings=ctypes.cast(mmap_ptr,ptr_settings)

# print(mmap_ptr)
# print(ptr_settings)
# print(ptr_settings.contents)

# ptr_settings.contents.RefreshRate_Hz=0xA9



validConfig,ini=vis.readConfigFile("test.ini")
if(validConfig):
    try:
        settings=visSt.PlayBackSettings(ini["PlayBackSettings"])
        settings.setRefreshRate(30)
        imageMap=vis.createMapFromFile(ini)

        onesImage=np.ones(imageMap.shape,imageMap.dtype)
        for i in range(0,10):
            imageMap[:]=i*25*onesImage
            settings.setFrameNumber(i)
            time.sleep(1)
    except Exception as e:
        print(e)
        raise RuntimeError("Unhandled Exception: Closing")
else:
    raise ValueError("Invalid Configuration File")


# print("Program Halted Successfully")
# sys.exit()
