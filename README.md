# Imdbapp
A Django based Web application that indexes all movies which automatically syncs on running application. 
  
**After initial setup requires no internet connection can be accesed when offline.**

### Installations
```
pip install -r requirements
```

### Setting Up
```
python manage.py makemigrations

python manage.py migrate --run-syncdb

python manage.py createsuperuser


#To Sync data in DB
All data will automatically sync into db once `python manage.py runserver` command executed. 

## Let's Start
```
python manage.py runserver or python manage.py runserver 0.0.0.0:8000
go to 127.0.0.1:8000
```
**By using runserver 0.0.0.0:8000 user can access it from any device connected to the same network** 
## Demo:

Users can only watch movies but admins can add delete or update movies from front-end as well as from admin panel.

**Search:**  
User can search movies based on Name and Genre.  

## Admin Access
Movies can be deleted or edited through the admin panel at **127.0.0.1:8000/admin**
But for that you will need to set up a superuser

```
python manage.py createsuperuser
```
And now you can delete or edit movies from the admin panel using the username and password you set. 

## API
This allows user to get get relevent movie information in form of JSON.
All requests should be made to:
`127.0.0.1:8000/movies/api`  
Movies data can be requested based on ***Name*** or ***Year*** or both.  
`127.0.0.1:8000/movies/api/name=name&g=genre`  
Both these parameters are optional
### Request: **127.0.0.1:8000/movies/api/name=star&g=music** 
### Response:

`[
    {
        "director": "Bobby Quinn",
        "imdb_rating": 8.3,
        "name": "The Tonight Show Starring Johnny Carson",
        "genre": "'Comedy', ' Music', ' Talk-Show'"
    },
    {
        "director": "Bruce Gowers",
        "imdb_rating": 4.8,
        "name": "American Idol : The Search for a Superstar",
        "genre": "'Game-Show', ' Music', ' Reality-TV'"
    }
]`

