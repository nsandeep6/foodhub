from django.db import models


# Create your models here.
class vendor(models.Model):
    vendor_name=models.CharField(max_length=50)
    vendor_email=models.EmailField()
    shop_name=models.CharField(max_length=50)
    shop_license=models.ImageField(blank=True,upload_to='licimg')
    shop_add=models.CharField(max_length=50)
    shop_phone_no=models.IntegerField()
    password1=models.CharField(max_length=20)
    password2=models.CharField(max_length=20)
    is_approved=models.BooleanField(default=False)




class customer(models.Model):
    usr_name=models.CharField(max_length=20)
    usr_first_name=models.CharField(max_length=20,default=None,blank=True,null=True)
    usr_last_name=models.CharField(max_length=20,default=None,blank=True,null=True)
    usr_email=models.EmailField()
    usr_phone_no=models.IntegerField()
    usr_add=models.CharField(max_length=100)
    pswd1=models.CharField(max_length=20)
    pswd2=models.CharField(max_length=20)