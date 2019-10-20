# Tathva-19 - Workshop "Introduction to Django"

**Please note:** After downloading this repo please add a change in *mysite/mysite/settings.py*  
                 please hash the line mentioned below:
```
# DATABASES['default'] = dj_database_url.config()

```

## How to get started
{we will be using terminal for most of the operations.}

### 1. Create a folder Blog using $: mkdir Blog

## In said folder create a virtual venv with python3

### 2. Create a Virtualenv by typing in

```
$: virtualenv -p python3 {env-name}
```

### 3. Install pip.

```
$:sudo apt-get install python-pip
```

### 4. Activate the virtual-env by

```
$: . ./{env-name}/bin/activate
```

### 5. Install Django

```
$:pip install django

$:pip install dj-database-url
```

### 6. Create a requirements file

```
$: pip freeze > requirements.txt
```

### 7.Let's start building Django:

```$: django-admin startproject mysite```


### 8.Changes to settings.py file in mysite/mysite/settings.py

```
TIME_ZONE = 'Asia/Kolkata'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
```

### 9. Creating a Database

```
$: python manage.py migrate
```

### 10.How to create a seperate application 

Here we going to call the app as blog 

```
$: python manage.py startapp {application-name}
```

### 11. Run Server

```
$: python manage.py runserver
```

These are the very basics of setting up a Django module.
Hope you enjoy the workshop on how to create a small webpage using Django.

# The rest of the tutorial will be added in the next few days 
