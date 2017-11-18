from django.contrib.auth.models import Permission, User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Site(models.Model):
    category = models.ForeignKey(Category, related_name='sites', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)
    site_logo = models.FileField()

    def __str__(self):
        return self.name + ' - ' + self.address


class Comment(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    rating = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return 'self.owner.__str__' + ' - ' + self.rating
