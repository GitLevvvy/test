from django.db import models



class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.username