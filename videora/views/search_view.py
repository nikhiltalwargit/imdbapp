
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from ..models import Movie
import os
import re

def search_movie(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if not request.POST['search']:
                return redirect('logged_in')
            if '-w' in request.POST['search']:
                Q=re.findall('(.*)\s+-w',request.POST['search'])
                if not Q:
                    movies=Movie.objects.all()
                    return render(request,'main.html',{'movies':movies})
                else:
                    Q=Q[0]
                    list1=Movie.objects.filter(popularity__contains=Q)
                    list2=Movie.objects.filter(director__contains=Q)
                    list3=Movie.objects.filter(imdb_rating__contains=Q)
                    list4=Movie.objects.filter(name__contains=Q)
                    list5=Movie.objects.filter(genre__contains=Q)

            else:
                Q=request.POST['search']
                list1=Movie.objects.filter(popularity__contains=Q)
                list2=Movie.objects.filter(director__contains=Q)
                list3=Movie.objects.filter(imdb_rating__contains=Q)
                list4=Movie.objects.filter(name__contains=Q)
                list5=Movie.objects.filter(genre__contains=Q)
            res=list(set(list1)^set(list2)^set(list3)^set(list4)^set(list5))
            context={
                'movies':res,
            }
            return render(request,'main.html',context)
    return redirect('logged_in')