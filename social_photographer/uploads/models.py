from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    price = models.BigIntegerField() # satoshis
    tuit = models.CharField(max_length=200)# id
    shot = models.ImageField(upload_to='showcase_pics')
    # owner = models.ForeignKey(User) # Check
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):             # __unicode__ on Python 2
        return self.name