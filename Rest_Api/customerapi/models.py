from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models


class Customer(models.Model):
    cust_name = models.CharField(max_length=250,default='Ram')
    cust_address = models.TextField(max_length=400,default = 'JayaNagar Bangalore')
    cust_dept = models.CharField(max_length=250, default ='Sales')
