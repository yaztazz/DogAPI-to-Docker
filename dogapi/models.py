from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50, choices=[('Tiny', 'Tiny'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])
    friendliness = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    trainability = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    sheddingamount = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    exerciseneeds = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)
