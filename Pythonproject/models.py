from django.db import models

class userinfo(models.Model):
    Name = models.CharField(max_length = 30)
    Email =  models.EmailField()
