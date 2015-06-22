import ConfigParser
import os

CONFIG_DIR = "config"
CONFIG_FILE = "config.cfg"
CONFIG = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', CONFIG_DIR, CONFIG_FILE)

def getkeys():
    cfgp = ConfigParser.ConfigParser()
    with open(CONFIG) as config:
        cfgp.readfp(config)
        return cfgp.items('twitter')
