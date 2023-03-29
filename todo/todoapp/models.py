from django.db import models
import datetime

# Create your models here.

class taskList(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name 