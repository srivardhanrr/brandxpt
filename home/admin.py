from django.contrib import admin

from home.models import Service, ServiceDetail

# Register your models here.
admin.site.register(Service)
admin.site.register(ServiceDetail)