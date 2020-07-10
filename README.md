# Django-Applications

## -> Logging in Django Applications

Create a simple django application and run it
```
$ django-admin startproject LoggingDemoApp
$ cd LoggingDemoApp
$ python manage.py runserver
```
Now you can see the admin page when you hit http://localhost:8000 url

Now create a module app inside LoggingDemoApp
```
$ python manage.py startapp welcome
```

Lets add the support of Logging
Add the below code snippets in the /welcome/views.py file
```
import logging
import logging.handlers as handlers
import time

# Creation of logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Here we define our formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# This settings rotates the log file every minute
logHandler = handlers.TimedRotatingFileHandler('debug.log', when='M', interval=1, backupCount=0)
logHandler.setLevel(logging.INFO)
logHandler.setFormatter(formatter)

# Create logger for Console
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(level=logging.INFO)
consoleHandler.setFormatter(formatter)

# Add both Console and File handers to logger
logger.addHandler(logHandler)
logger.addHandler(consoleHandler)
```

Now log the error, info, debug into the console or file by using the below code
```
logger.error("Test Logging !!")
logger.debug("Debug Log !!")
logger.info("Info Log !!")
```
Before running the application update the /LoggingDemoApp/urls.py and /welcome/urls.py files 
Now you can check the LoggingDemoApp directory for log files.
```
debug.log
debug.log.2020-07-10_19-12
```

Simple File handler - this creates the file and appends the log
```
fileHandler = logging.FileHandler('debug.log')
```
Roll the log file when it reaches size of 1MB
```
logHandler = handlers.RotatingFileHandler('debug.log', maxBytes=1024, backupCount=0)
```
Roll log file every day, other values  ( S,M,H,D,W0,W1,midnight)
```
logHandler = handlers.TimedRotatingFileHandler('debug.log', when='midnight', interval=1)
logHandler.suffix = "%Y-%m-%d_%H-%M-%S"
```
