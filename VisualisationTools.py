
import numpy as np 
import sys
import os

import configparser

  

def readConfigFile(ini_directory):
    config = configparser.ConfigParser()
    config.optionxform = str
    try:
        config.read(ini_directory)
        return True,config
    except Exception as err:
        print(err)
        return False,err


def createMapFromFile(ini):
    '''
    Create mmap file in a tmp directory
    '''
    try:
        os.mkdir("tmp")
    except FileExistsError:
        pass
    except Exception as e:
        print(e)
        sys.exit("Unhandled Exception - Closing")  
    baseImage=np.memmap('tmp/base',
                        dtype='uint8',
                        mode='w+',
                        shape=(100,200))

    return baseImage

def readMapFromFile(ini):
    '''
    reade mmap file in a tmp directory
    '''
    baseImage=np.memmap('tmp/base',
                        dtype='uint8',
                        mode='r',
                        shape=(100,200))

    return baseImage    