from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/service/')
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class ServiceDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Link to Service model
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/service/')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Optional for author tracking
