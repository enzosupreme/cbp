from django.contrib import admin

# Register your models here.
from .models import Key, Santa, Gift

admin.site.register(Key)
admin.site.register(Santa)
admin.site.register(Gift)