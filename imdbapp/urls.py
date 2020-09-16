from django.conf.urls import url,include
from django.contrib import admin
from videora import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name="index"),
    #movies/
    url(r'^movies/',include('videora.urls')),

    #register/
    url(r'^register/$',views.register,name="register"),
    #logged_in/
    url(r'^logged_in/$',views.logged_in,name="logged_in"),

    url(r'^logged_out/$',views.log_out,name="log_out"),

    url(r'^search/$',views.search_movie,name="search"),

    url(r'^add-movie$',views.create_view,name="addmovie"),

    url(r'^update-movie/(?P<_id>\d+)/$',views.update_view,name="updatemovie"),

    url(r'^delete-movie/(?P<_id>\d+)/$',views.delete_view,name="deletemovie"),
  

]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
