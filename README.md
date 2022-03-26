# Travel_Agency
===================

SDA Python Tirana AL 4 django Final Project

Setup
-----

Clone the repository

```
git clone https://github.com/adrianapalushi/travel_agency.git
```

Create a virtual environment

```
python -m venv venv
```

Active the virtual environment

On Linux/MacOS

```
. venv/bin/active
```

On Windows when using powershell

```
. venv/Scripts/activate
```

After activating the virtual environment install the dependencies

```
python -m pip install -r requirements.txt
```

Run the migrations

```

python manage.py migrate
```


python manage.py createcategories
python manage.py createfakeproducts 100


Run the development server

```
python manage.py runserver
```

In your browser visit http://localhost:8000 to view the site
