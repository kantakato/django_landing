from django.db import models

class Landing(models.Model):
    email = models.EmailField()
    
    class Meta:
        db_table = 'landing'