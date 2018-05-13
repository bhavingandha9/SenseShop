from django.template import loader
from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.shortcuts import redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from myadmin.models import product,order_details,complaint,temp_cart
from login.models import customer
from django.core.urlresolvers import reverse_lazy,reverse
from . import app_settings
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist

class Userhome(generic.ListView):
    template_name = 'index.html'
    model = product
    context_object_name = 'product'
    
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('user'):
            a = 'hello'
        else:
            return redirect('user')
        return super(Userhome, self).dispatch(request,*args, **kwargs)

    def get_queryset(self):
        return product.objects.all()
        
class OrderIndexView(generic.ListView): 
    template_name = 'orderdetails.html'
    context_object_name = 'order'
    model = order_details

    def get_queryset(self): 
        user = self.request.session['user']        
        user_object = customer.objects.get(email = user )
        return order_details.objects.filter(c_id_id=user_object.id)
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('user'):
            a = 'hello'
        else:
            return redirect('index')
        return super(OrderIndexView, self).dispatch(request,*args, **kwargs)

class OrderDetailView(generic.DetailView):
    model = order_details
    template_name = 'user_home.html'
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('user'):
            a = 'hello'
        else:
            return redirect('index')
        return super(OrderDetailView, self).dispatch(request,*args, **kwargs)

def complaint_form(request):
    template = loader.get_template('add/complaint_form.html')
    context = {
                    'o_id':request.GET['o_id'], 
              }
    return HttpResponse(template.render(context,request))

def ComplaintCreate(request):
    if request.session.has_key('user'):
        a = request.session['user']
        b = customer.objects.get(email = a )
        order_id = request.POST.get('o_id')
        msg = request.POST.get('cm_msg')
        newComplaint = complaint(c_id_id=b.id,o_id_id=order_id,cm_msg=msg)
        newComplaint.save()
       
        #return HttpResponse(b.id)
        return redirect('user_order')
    else:
         return redirect('index')
        


# class ComplaintCreateView(CreateView):
#     template_name = 'add/complaint_form.html'
#     model = complaint
#     fields = ['cm_msg','o_id']
#     success_url = reverse_lazy('myadmin') 
#     def dispatch(self,request ,*args, **kwargs):
#         if request.session.has_key('user'):
#             a = request.session['user']
#         else:
#             return redirect('index')
#         return super(ComplaintCreateView, self).dispatch(request,*args, **kwargs)
    
    def form_valid(self,form):
        a = self.request.session['user']
        b = customer.objects.get(email = a )
        form.instance.c_id_id = b.id
        return super(ComplaintCreateView, self).form_valid(form)
       
class Cart(generic.ListView):
    template_name = 'cart.html'
    model = temp_cart
    context_object_name = 'temp_cart'
    
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('user'):
            a = 'hello'
        else:
            return redirect('user')
        return super(Cart, self).dispatch(request,*args, **kwargs)
    def get_queryset(self):
        a = self.request.session['user']        
        b = customer.objects.get(email = a )       
        return temp_cart.objects.filter(c_id_id=b.id)


def logout(request):
            del request.session['user']
            return redirect('index')

def add2cart(request):
    if request.GET["product_id"]:
        product_id = request.GET["product_id"]
        a = request.session['user']
        b = customer.objects.get(email = a )
        try:
            temp_cart.objects.get(pro_id_id=int(product_id),c_id_id=b.id)
            temp_cart.objects.filter(c_id_id=b.id,pro_id_id=product_id).update(quantity = F("quantity") + 1)
            return redirect('user')
        except ObjectDoesNotExist:
            cart = temp_cart(pro_id_id=int(product_id),c_id_id=b.id,quantity=1,flag=0)
            cart.save()
            return redirect('user') 
 
def quantity_inc(request):
    if request.GET["product_id"]:
        product_id = request.GET["product_id"]
        a = request.session['user']
        b = customer.objects.get(email = a )
        temp_cart.objects.filter(c_id_id=b.id,pro_id_id=product_id).update(quantity = F("quantity") + 1)
        return redirect('cart')

def quantity_dec(request):
    if request.GET["product_id"]:
        product_id = request.GET["product_id"]
        a = request.session['user']
        b = customer.objects.get(email = a )
        temp_cart.objects.filter(c_id_id=b.id,pro_id_id=product_id).update(quantity = F("quantity") - 1)
        return redirect('cart')

def remove_product(request):
    if request.GET["product_id"]:
        product_id = request.GET["product_id"]
        a = request.session['user']
        b = customer.objects.get(email = a )
        temp_cart.objects.filter(c_id_id=b.id,pro_id_id=product_id).delete();
        return redirect('cart')

def payment(request):
    user = request.session['user']
    user_object = customer.objects.get(email = user )
    cart = temp_cart.objects.filter(c_id_id=user_object.id)
    amount = 0
    for cart_data in cart:
        amount = amount + cart_data.pro_id.pro_price

    request.session['amount'] = str(amount)   
    request.session.modified = True
    return redirect(reverse('payment:process'))

def checkout(request):
    user = request.session['user']
    user_object = customer.objects.get(email = user )
    cart = temp_cart.objects.filter(c_id_id=user_object.id)
    product = []
    quantity = []
    for cart_data in cart:
        product.append(cart_data.pro_id_id)
        quantity.append(cart_data.quantity)

    entry = order_details(pay_id_id = 1 , c_id = user_object ,products = product, quantity= quantity, flag = 0)
    entry.save()    
    temp_cart.objects.filter(c_id_id=user_object.id).delete()           
    return redirect('user')

def search(request):
    if request.method == "POST":
        query = request.POST['query'] 
        if query: 
                product_data = product.objects.filter(pro_name__icontains=query)
                template = loader.get_template('index.html')
                context = {
                    'product':product_data, 
                }
                return HttpResponse(template.render(context,request)) 
        else:
            return redirect('index')
    else:
            return redirect('index')

def service_worker(request):
    response = HttpResponse(open(app_settings.PWA_SERVICE_WORKER_PATH).read(), content_type='application/javascript')
    return response 

def manifest(request):
    return render(request, 'manifest.json', {
        setting_name: getattr(app_settings, setting_name)
        for setting_name in dir(app_settings)
        if setting_name.startswith('PWA_')
})
