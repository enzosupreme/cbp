from django.contrib import admin

from .models import Race, Affiliation, NonPlayerCharacter, Enemy, Stat

admin.site.register(Race)
admin.site.register(Stat)
admin.site.register(Enemy)
admin.site.register(Affiliation)
admin.site.register(NonPlayerCharacter)


