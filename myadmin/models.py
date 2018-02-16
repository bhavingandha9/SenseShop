from django.db import models
from login.models import customer as a
from django.core.urlresolvers import reverse
#make sure all colums names are in deCAPS

class product(models.Model):
    pro_name = models.CharField(max_length=250)
    au_id = models.DecimalField(max_digits=20,decimal_places=0)
    pro_price = models.DecimalField(max_digits=5, decimal_places=0)
    prodct_dec =models.CharField(max_length=1000)
    flag =models.DecimalField(max_digits=2,decimal_places=0)

    def get_absolute_url(self):
        return reverse('product')

    def __str__(self):
      return self.pro_name

class stock(models.Model):
    pro_id = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=3,decimal_places=0)
    flag = models.DecimalField(max_digits=2,decimal_places=0)
    def __str__(self):
      return str(self.pro_id)
    def get_absolute_url(self):
        return reverse('stock')

class warehouse_stock(models.Model):
    s_id = models.ForeignKey(stock, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=3,decimal_places=0)
    flag = models.DecimalField(max_digits=2,decimal_places=0)
    def __str__(self):
      return str(self.s_id)

class retail_stock(models.Model):
    s_id = models.ForeignKey(stock, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=100,decimal_places=0)
    flag = models.DecimalField(max_digits=2,decimal_places=0)
    def __str__(self):
      return str(self.s_id)

class feedback(models.Model):
    email = models.CharField(max_length=150)
    mobile = models.DecimalField(max_digits=10,decimal_places=0)
    f_msg = models.CharField(max_length=1000)
    flag =models.DecimalField(max_digits=2,decimal_places=0)
    def __str__(self):
      return self.email+'-' +self.f_msg
    def get_absolute_url(self):
        return reverse('feedback')

class temp_cart(models.Model):
    pro_id = models.ForeignKey(product)
    c_id = models.ForeignKey(a)
    quantity = models.DecimalField(max_digits=50,decimal_places=0)
    total_amount = models.DecimalField(max_digits=100,decimal_places=0)
    flag =models.DecimalField(max_digits=2,decimal_places=0)
    def __str__(self):
      return str(self.pro_id)+'-' +str(self.c_id)+'-'
    def get_absolute_url(self):
        return reverse('temp_cart')

class payments(models.Model):
    tc_id = models.ForeignKey(temp_cart)
    c_id = models.ForeignKey(a)
    amount = models.DecimalField(max_digits=100, decimal_places=0)
    transaction_id = models.DecimalField(max_digits=150,decimal_places=0)
    flag =models.DecimalField(max_digits=2,decimal_places=0)
    def __str__(self):
      return str(self.tc_id) +'-' +str(self.c_id)+'-' +str(self.transaction_id)
    def get_absolute_url(self):
        return reverse('payments')

class order_details(models.Model):
    tc_id = models.ForeignKey(temp_cart)
    pay_id = models.ForeignKey(payments)
    c_id = models.ForeignKey(a)
    flag =models.DecimalField(max_digits=2,decimal_places=0)
    def __str__(self):
      return str(self.tc_id) +'-' + str(self.pay_id) +'-' +str(self.c_id)
    def get_absolute_url(self):
        return reverse('order_details')

class complaint(models.Model):
    email = models.CharField(max_length=150)
    mobile = models.DecimalField(max_digits=10,decimal_places=0)
    cm_msg = models.CharField(max_length=1000)
    o_id = models.ForeignKey(order_details)
    flag = models.DecimalField(max_digits=2,decimal_places=0)
    def __str__(self):
      return str(self.email)
    def get_absolute_url(self):
        return reverse('complaint')
