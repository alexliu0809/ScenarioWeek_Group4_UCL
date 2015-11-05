from django.db import models
from django.utils import timezone

# Create your models here.

class Todolist(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=600)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def str(self):
        return Title


class Task(models.Model):
    Todolist = models.ForeignKey(Todolist)
    Task_text = models.CharField(max_length=600)
    Due_Date = models.DateField('date due')
    Priority = models.IntegerField(default=0)