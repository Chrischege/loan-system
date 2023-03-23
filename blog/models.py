from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class post(models.Model):
    
    #title=models.CharField(max_length=100)
    date_posted=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    id_number = models.IntegerField( null=False,blank=True)
     #loan name
    loan_name = models.CharField(max_length=100)
    #loan amount
    loan_amount = models.IntegerField()
    #loan interest
    loan_interest = models.FloatField(default=0.02)
    #loan duration
    loan_duration = models.IntegerField(default=2)


    def __str__(self):
        return self.loan_name
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
# def a loan model for a loaning system
