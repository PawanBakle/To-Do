from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
#     def __str__(self):
#         return self.username

class TaskList(models.Model):
    CHOICE = (('High','High'),
              ('Medium','Medium'),
              ('Low','Low'))
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    date = models.DateField(blank=True,null=True)
    tags = models.CharField(max_length =200,null = True,choices=CHOICE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title + self.description