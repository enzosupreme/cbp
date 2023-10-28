from django.contrib import admin

from .models import Category, Project, Service, ServiceRequest,  Menu_item, About, Image, Garden_Pic

admin.site.register(Menu_item)
admin.site.register(Category)
admin.site.register(About)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(ServiceRequest)
admin.site.register(Image)
admin.site.register(Garden_Pic)