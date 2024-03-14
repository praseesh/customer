# from django.db import models

# # Create your models here.
# class Customer(models.Model):
#     firstname=models.CharField(max_length=20, default= 'Firstname', verbose_name="Name",unique=True)
#     lastname=models.CharField(max_length=20, verbose_name="Surname", blank=True)
#     address=models.CharField(max_length=20)
#     phno=models.BigIntegerField(default=0,verbose_name="phone Number")

#     def __str__(self):
#         return self.firstname
    
#     class Meta:
#         db_table='demoapp_Customer'


from django.db import models

class Customer(models.Model):
    firstname = models.CharField(max_length=20, default='', verbose_name="Name", unique=True)
    lastname = models.CharField(max_length=20, verbose_name="Surname", blank=True)
    address = models.CharField(max_length=20)
    phno = models.BigIntegerField(verbose_name="Phone Number", blank=True, null=True)

    def __str__(self):
        return self.firstname
    
    class Meta:
        db_table = 'demoapp_Customer'
