from django.apps import AppConfig
from fixture import create_fixture
import subprocess
import sys




class VideoraConfig(AppConfig):
    name = 'videora'

    '''
    Running sync database script  on startup application

    '''
    def ready(self):
        if 'runserver' in sys.argv:
            db_sync_file = create_fixture('imdb.json')
            print ('Database sync ready...')
            command = ['python', 'manage.py', 'loaddata',db_sync_file]
            print ('Database synced Sucessfully!')
            subprocess.run(command)
        return True
