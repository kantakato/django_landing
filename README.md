django_landing
==============
This project is ONLY landing web site for Django(python).  
You can make a web site based on the method of lean startup.  
Django-landing will also work on heroku(Of course on local).  
This project consists [Python](http://www.python.org/) 2.7.x, [Django](https://www.djangoproject.com/) 1.5.1 and [TwitterBootstrap](http://twitter.github.io/bootstrap/) 2.3.1.

## How to use ##
### 1. Download Zip ###
Download django-landing zip files and unzip.  

### 2. Create virtual environment for python ###
Next is Change directory to unzipped directory.
And create virtualenv setting by CLI.  
`$ > virtualenv venv --distribute`  
Change to virtual environment of python.  
`$ > source venv/bin/activate`  
Check the command line is starting from character (venv).  
`(venv) $ >`  

### 3. Install requirements.txt ###
Before you work project on local machine, you must install some modules in requirements.txt by pip.  
`(venv) $ > pip install -r requirements.txt`  

### 4. Test run ###
If you run django-landing project on local machine, comment out database setting in settings.py.  
```python
    #import dj_database_url  
    #DATABASES['default'] =  dj_database_url.config()  
```
,and create local database.  
`(venv) $ > python manage.py syncdb`

So you can run on local machine by  
`(venv) $ > python manage.py runserver`  
And see django-landing [localhost:8000](http://localhost:8000).  

If you made heroku environment, you can also run django-landing by foreman.  
`(venv) $ > foreman start`

### 5. Work on Heroku ###
If you want to work django-landing project on heroku, you have to make [heroku](https://www.heroku.com/) account.  
Install heroku toolbelt, and login.[Getting Started with Heroku](https://devcenter.heroku.com/articles/quickstart)  
After procedure is usual.[Store app in Git,Deploy to heroku etc](https://devcenter.heroku.com/articles/django#store-your-app-in-git).
