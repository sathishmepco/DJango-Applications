from django.shortcuts import render
from django.http import HttpResponse
import logging
import logging.handlers as handlers
import time

#Creation of logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Here we define our formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#This settings rotates the log file every minute
logHandler = handlers.TimedRotatingFileHandler('debug.log', when='M', interval=1, backupCount=0)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(level=logging.INFO)
consoleHandler.setFormatter(formatter)

logHandler.setLevel(logging.INFO)
logHandler.setFormatter(formatter)

logger.addHandler(logHandler)
logger.addHandler(consoleHandler)

def home(request):
    logger.error("Test Logging !!")
    return HttpResponse("Welcome to Home Page !!!")