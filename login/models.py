from django.db import models

class customer(models.Model):
    cname = models.CharField(max_length=100,default='a')
    email = models.CharField(max_length=250,default='a')
    password = models.CharField(max_length=250,default='a')
    mobile_no = models.DecimalField(max_digits=10,decimal_places=0,default='a')
   # dob = models.DateField()
    address = models.CharField(max_length=500,default='a')
    au_id = models.DecimalField(max_digits=200,decimal_places=0,default='a')
    cflag = models.DecimalField(max_digits=2,decimal_places=0,default='a')
    def __str__(self):
      return self.email
    def get_absolute_url(self):
        return reverse('customer')
# class myadmintable(models.Model):
#     email = models.CharField(max_length=250,default='a')
#     password = models.CharField(max_length=250,default='a')
#     au_id = models.DecimalField(max_digits=200,decimal_places=0,default='a')
#     flag = models.DecimalField(max_digits=2,decimal_places=0,default='a')
#     def __str__(self):
#           return self.email