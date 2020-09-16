from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import MovieSerializer
from .models import Movie

#/movies/api
@api_view(['GET','POST'])
def API_res(request,name,genre):
    if request.method == 'GET':
        if genre and name:
            movies=Movie.objects.filter(name__contains=name,genre__contains=genre)
        elif name:
            movies=Movie.objects.filter(name__contains=name)
        else:
            movies=Movie.objects.filter(genre=genre)
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)
