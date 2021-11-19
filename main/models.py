from django.db.models import *

# Create your models here.
class BaseStation(Model):
    secret_key = CharField(max_length = 20, unique = True)
    data = CharField(max_length = 250, default = '')
