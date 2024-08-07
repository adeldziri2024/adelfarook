
- ✅ `Up-to-date dependencies`
- ✅ Database: `sqlite`
- ✅ UI-Ready app, Django Native ORM
- ✅ `Session-Based authentication`, Forms validation

<br />



<br />

## Table of Contents



<br />

## Demo



<br />

## Quick start

> UNZIP the sources or clone the repository. After getting the code, open a terminal and navigate to the working directory, with product source code.

```bash
$ git clone https://github.com/app-generator/django-black-dashboard.git
$ cd django-black-dashboard
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env / python -m venv env
$ source env/bin/activate / source env/Scripts/activate   / source env\Scripts\activate
$ pip3 install -r requirements.txt
```

*************************************************
source env/Scripts/activate


<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## Documentation



<br />

## File Structure
Within the download you'll find the following directories and files:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- Django bootstrapper `manage.py` uses `core/settings.py` as the main configuration file
- `core/settings.py` loads the app magic from `.env` file
- Redirect the guest users to Login page
- Unlock the pages served by *app* node for authenticated users

<br />



<br />




**********************************
**********************************
asgiref         3.8.1
autopep8        1.6.0
dj-database-url 0.5.0
Django          5.0.7
django-environ  0.8.1
django-fsm      3.0.0
gunicorn        20.1.0
numpy           2.0.1
pandas          2.2.2
pendulum        3.0.0
pip             24.2
pycodestyle     2.8.0
python-dateutil 2.9.0.post0
pytz            2024.1
setuptools      69.0.3
six             1.16.0
sqlparse        0.4.2
time-machine    2.14.2
toml            0.10.2
tzdata          2024.1
wheel           0.43.0
whitenoise      5.3.0
*********************************
*********************************
