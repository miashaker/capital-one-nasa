from django.db import models
from django.contrib.auth.models import User

class Search(models.Model):
    searcher = models.ForeignKey(User, on_delete=models.PROTECT, blank=True )
    text = models.CharField(max_length=500)
# Create your models here.
