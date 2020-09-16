from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import UserManager
from safedelete import safedelete_mixin_factory, SOFT_DELETE

safe_delete_mixin = safedelete_mixin_factory(policy=SOFT_DELETE)
safe_delete_admin_mixin = safedelete_mixin_factory(policy=SOFT_DELETE, manager_superclass=UserManager)

class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value' : self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)


class Movie(safe_delete_admin_mixin):
    popularity = MinMaxFloat(min_value=0.0, max_value=100.0)
    director = models.CharField(max_length=50,default=None)
    imdb_rating = MinMaxFloat(min_value=0.0, max_value=10.0)
    name = models.CharField(max_length=300)
    genre = models.CharField(max_length=300,help_text = "Comma seperated values Ex: Family, Fantasy, Musical")

    def __str__(self):
        return self.name


