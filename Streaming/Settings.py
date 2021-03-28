import os
import configparser



def readConfigFile(ini_directory):
    print(os.path.isfile(ini_directory))
    config = configparser.ConfigParser()
    config.optionxform = str
    try:
        config.read(ini_directory)
        return True,config
    except Exception as err:
        print(err)
        return False,err