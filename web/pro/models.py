from django.db import models

class Task(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False, null=True, blank=True)
    number=models.CharField(max_length=100, blank=False, null=False)
    create_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Company(models.Model):
    name= models.CharField(max_length=200, null=True, blank=True)
    country=models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)
    numbers = models.CharField(max_length=100)
    images = models.ImageField(upload_to="images/", null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
