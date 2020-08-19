from django.db import models

# Create your models here.
class Qari(models.Model):
    name = models.CharField(max_length=300)
    days = models.CharField(max_length=200)
    day1 = models.TextField(default="")
    day2 = models.TextField(default="")
    day3 = models.TextField(default="")
    day4 = models.TextField(default="")
    day5 = models.TextField(default="")
    timings = models.CharField(max_length = 400)

    def __str__(self):
        return self.name 