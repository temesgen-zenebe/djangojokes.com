from django.contrib import admin
from .models import Joke
# Register your models here.


@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    model = Joke
    list_display = ['question', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):

        """if obj: # editing an existing object
            return ('created', 'updated')"""

        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
            
        return ()