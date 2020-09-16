from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        # fields = '__all__' #for all of them
        fields = ('director','imdb_rating','name','genre')
