from __future__ import unicode_literals

from django.db import models

# Create your models here.
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class Profile(Model):
    username= columns.Text(primary_key=True)
    address= columns.Text()
    company= columns.Text()
   

    def __str__(self):
        return self.username
