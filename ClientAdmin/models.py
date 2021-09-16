from django.db import models

# Create your models here.
class admin(models.models):
    AdminID= models.AutoField(primary_Key= True)
    AdminName= models.CharField(max_length= 500)

    class client(models.models):
    ClientID= models.AutoField(primary_Key= True)
    ClientName= models.CharField(max_length= 500)
    ClientDOJ= models.DateField()
    ClientDept= models.CharField(max_length= 500)
    ClientFile= models.CharField(max_length= 500)




