from django.contrib import admin

# Register your models here.
from .models import Key, Santa, Gifter

admin.site.register(Key)
admin.site.register(Santa)
admin.site.register(Gifter)