from django.db import models

# Create your models here.
class user_info(models.Model):
    def __str__(self):
        return self.user_name
    
    user_name = models.CharField(max_length=60)
    password = models.CharField(max_length=30)
    