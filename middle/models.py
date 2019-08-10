from django.db import models

# Create your models here.

class Users(models.Model):
    u_name=models.CharField(max_length=200)
    u_school=models.CharField(max_length=200)
    u_major=models.CharField(max_length=200)
    u_interest=models.CharField(max_length=200)

class Apply(models.Model):
    #a_nowuser=models.ForeignKey(Users, on_delete=models.CASCADE)
    a_company=models.CharField(max_length=200)
    a_interset=models.CharField(max_length=200)
    a_qone_q=models.TextField(max_length=1000)
    a_qone=models.TextField(max_length=2000)
    a_qtwo_q = models.TextField(max_length=1000)
    a_qtwo=models.TextField(max_length=2000)
    a_qthree_q = models.TextField(max_length=1000)
    a_qthree=models.TextField(max_length=2000)
    a_qfour_q = models.TextField(max_length=1000)
    a_four=models.TextField(max_length=2000)
    a_qfive_q = models.TextField(max_length=1000)
    a_five=models.TextField(max_length=2000)
