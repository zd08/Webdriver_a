import logging
import logging.config
import os

parentDirPath = os.path.dirname(os.path.abspath(__file__))
#print(parentDirPath)
logging.config.fileConfig(parentDirPath+u"\Logger.conf")


logger = logging.getLogger('example02')#或者example01

def debug(message):
    logger.debug(message)

def info(message):
    logger.info(message)

def warning(message):
    logger.warning(message)
