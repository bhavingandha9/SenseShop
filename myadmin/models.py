from django.db import models
from login.models import customer as a
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
 
class product(models.Model):
    pro_name = models.CharField(max_length=250, unique=True)
    au_id = models.DecimalField(max_digits=20,decimal_places=0,unique=True)
    pro_price = models.DecimalField(max_digits=5, decimal_places=0)
    prodct_dec =models.CharField(max_length=1000)
    flag =models.DecimalField(max_digits=2,decimal_places=0,null=True,blank=True,default=0)

    def get_absolute_url(self):
        return reverse('product')

    def __str__(self):
      return self.pro_name
    def __unicode__(self):
        return unicode(self.pk)


class stock(models.Model):
    pro_id = models.ForeignKey(product, on_delete=models.CASCADE,related_name='product_primary')
    quantity = models.DecimalField(max_digits=3,decimal_places=0)
    flag = models.DecimalField(max_digits=2,decimal_places=0,null=True,blank=True,default=0)
    def __str__(self):
      return str(self.pro_id)

    def __unicode__(self):
        return unicode(self.pk)
    def get_absolute_url(self):
        return reverse('stock')
  
    @receiver(post_save,sender=product)
    def update_stock(sender,instance,**kwargs):
        p = stock(pro_id_id=instance.pk,quantity=0,flag=0)
        p.save()
 
  
class temp_cart(models.Model):
    pro_id = models.ForeignKey(product)
    c_id = models.ForeignKey(a,default=0)
    quantity = models.DecimalField(max_digits=50,decimal_places=0) 
    flag =models.DecimalField(max_digits=2,decimal_places=0)
    
    def __str__(self):
      return str(self.pro_id)+'-' +str(self.c_id) 
    def get_absolute_url(self):
        return reverse('temp_cart')
 
class payment(models.Model): 
    c_id = models.ForeignKey(a,default=0)
    amount = models.DecimalField(max_digits=100, decimal_places=0)
    transaction_id = models.DecimalField(max_digits=150,decimal_places=0,unique=True)
    flag =models.DecimalField(max_digits=2,decimal_places=0,null=True,blank=True)
    def __unicode__(self):
        return unicode(self.pk)
    def __str__(self):
        return str(self.amount)


class order_details(models.Model): 
    pay_id = models.ForeignKey(payment,related_name='payment')
    c_id = models.ForeignKey(a,default=0)
    products = models.CharField(max_length=250,null=True,blank=True)
    quantity = models.CharField(max_length=250,null=True,blank=True)
    flag =models.DecimalField(max_digits=2,decimal_places=0)
    def __str__(self):
      return  str(self.pay_id) +'-' +str(self.c_id)
    def get_absolute_url(self):
        return reverse('order_details')

class complaint(models.Model):
    c_id = models.ForeignKey(a,default=0)
    o_id = models.ForeignKey(order_details)
    cm_msg = models.CharField(max_length=1000,null=True,blank=True)
    replay = models.CharField(max_length=1000,null=True,blank=True)
    flag = models.DecimalField(max_digits=2,decimal_places=0,null=True,blank=True,default=0)
    def __str__(self):
      return str(self.cm_msg)
    def get_absolute_url(self):
        return reverse('complaint')

class myadmin(models.Model): 
    email = models.CharField(max_length=250,default='a')
    password = models.CharField(max_length=250,default='a') 
    def __str__(self):
      return self.email
    def get_absolute_url(self):
        return reverse('myadmin')


#class warehouse_stock(models.Model):
#     s_id = models.ForeignKey(stock, on_delete=models.CASCADE)
#     quantity = models.DecimalField(max_digits=3,decimal_places=0)
#     flag = models.DecimalField(max_digits=2,decimal_places=0)
#     def __str__(self):
#       return str(self.s_id)

# class retail_stock(models.Model):
#     s_id = models.ForeignKey(stock, on_delete=models.CASCADE)
#     quantity = models.DecimalField(max_digits=100,decimal_places=0)
#     flag = models.DecimalField(max_digits=2,decimal_places=0)
#     def __str__(self):
#       return str(self.s_id)