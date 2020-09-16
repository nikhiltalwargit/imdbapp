from django.shortcuts import render, redirect
from django.shortcuts import (get_object_or_404, 
                              render, 
                              HttpResponseRedirect)
from ..models import Movie 
from ..forms import MovieForm 
  
  
def create_view(request): 
    if request.method == "POST":  
        form = MovieForm(request.POST)  
        if form.is_valid():
            form.save()  
            return redirect('/')
    else:  
        form = MovieForm()  
    return render(request,'operations/create_view.html',{'form':form})  
    

def update_view(request, _id): 
    obj = get_object_or_404(Movie, id = _id)  
    form = MovieForm(request.POST or None, instance = obj) 
    context= {'form': form}
    if form.is_valid(): 
        form.save() 
        return redirect('/')
    else:
        return render(request, 'operations/update_view.html', context)  


def delete_view(request, _id):
    movie = Movie.objects.get(id=_id)  
    movie.delete()  
    return redirect("/")  


