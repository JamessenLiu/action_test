from django.db import models

class Actions(models.Model):
    
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    
    class Meta:
        db_table = "action"
