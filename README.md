# Django-Applications
- [Logging in Django Application](#Logging-in-Django-Applications)
- [ReCaptcha Implementation in Django Application](#ReCaptcha-Implementation-in-Django-Application)
- [Django Simple Captcha](#Django-Simple-Captcha)

# Logging in Django Applications

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

# ReCaptcha Implementation in Django Application

Create a simple django application and run it
```
$ django-admin startproject ReCaptchaDemo
$ cd ReCaptchaDemo
$ python manage.py startapp Login
$ python manage.py runserver
```

Create form (index.html) using bootstrap 4
```
$ cd ReCaptchaDemo
create new directory "templates"
create a file index.html inside templates (add the html content)

#css
$ cd ReCaptchaDemo
create a new directory "static"
create a new directory "css" inside "static"
Copy the required css files inside "css" directory

#updates in ReCaptchaDemo/settings.py file
- update the DIRS and rest of the TEMPLATES are same
TEMPLATES = [
    {
        ...
        'DIRS':
            [
                os.path.join(BASE_DIR, 'templates')
            ],
        ...
    },
]

- add the following
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

- create new variable GOOGLE_RECAPTCHA_SECRET_KEY
GOOGLE_RECAPTCHA_SECRET_KEY = 'YOUR_PRIVATE_KEY'
```

Register for ReCaptcha and get SITE_KEY & SECRET_KEY
- Click this link to register website https://www.google.com/recaptcha/admin/create
- Enter the label "Demo Site 1"
- Select "reCAPTCHA v2" -- "I'm not a robot" tickbox
- Add "localhost" in domains
- Accept the reCAPTCHA Terms of Service
- Then submit to get SITE_KEY & SECRET_KEY

Update the keys in Django application
- Update SITE_KEY in index.html file.
- Update SECRET_KEY in ReCaptchaDemo/settings.py

Don't forget to do the changes in views.py & urls.py file.
<img src="/ReCaptchaDemo/django_recaptcha.png"/>


# Django Simple Captcha

Simple Captcha documentation https://django-simple-captcha.readthedocs.io/en/latest/usage.html

```
1. Installation
pip install  django-simple-captcha

2. Add captcha to the INSTALLED_APPS in your settings.py

3. Run python manage.py migrate

4. Add an entry to your urls.py:
urlpatterns += [
    url(r'^captcha/', include('captcha.urls')),
]
```
