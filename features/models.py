from django.db import models

# Create your models here.
class user_info(models.Model):
    def __str__(self):
        return self.user_name
    
    user_name = models.CharField(max_length=60)
    password = models.CharField(max_length=30)
    
class school_dropout_data(models.Model):
    
    
    principal_name = models.CharField(max_length=60)
    school_name = models.CharField(max_length=60)
    school_region = models.CharField(max_length=60)
    school_district = models.CharField(max_length=60)
    drop_out_number = models.IntegerField(default=0)

