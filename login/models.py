from django.db import models

class customer(models.Model):
    cname = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=250,null=True,blank=True)
    password = models.CharField(max_length=250,null=True,blank=True)
    mobile_no = models.DecimalField(max_digits=10,decimal_places=0,null=True,blank=True)
   # dob = models.DateField()
    address = models.CharField(max_length=500,null=True,blank=True)
    au_id = models.DecimalField(max_digits=200,decimal_places=0,default=0,null=True,blank=True)
    cflag = models.DecimalField(max_digits=2,decimal_places=0,default=0,null=True,blank=True)
    def __str__(self):
      return self.email
    def get_absolute_url(self):
        return reverse('index')
 