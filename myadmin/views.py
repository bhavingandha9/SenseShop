from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import product,complaint,stock,order_details,payment
from login.models import customer
from django.core.mail import send_mail
from paypal.standard.ipn.models import PayPalIPN


def index(request):
    if request.session.has_key('myadmin'):
        template = loader.get_template('admin_home.html')
        return HttpResponse(template.render(request))
    else:
        return redirect('index')
 
class CustomerCreateView(generic.CreateView):
    template_name = 'add/customer_form.html'
    model = customer
    fields = {'cname', 'email', 'password', 'mobile_no', 'address', 'au_id'}

    def dispatch(self, request, *args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(CustomerCreateView, self).dispatch(request, *args, **kwargs)
 
class CustomerIndexView(generic.ListView):
    template_name = 'customer.html'
    context_object_name = 'customer'
    model = customer
    paginate_by = 5

    def get_queryset(self):
        return customer.objects.all()

    def dispatch(self, request, *args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(CustomerIndexView, self).dispatch(request, *args, **kwargs)
 
class CustomerDetailView(generic.DetailView):
    template_name = 'detail/customer_detail.html'
    context_object_name = 'customer'
    model = customer

    def dispatch(self, request, *args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(CustomerDetailView, self).dispatch(request, *args, **kwargs)
 
class CustomerUpdateView(UpdateView):
    template_name = 'update/customer_update.html'
    model = customer
    fields = ['email', 'mobile_no']
    success_url = reverse_lazy('customer')

    def dispatch(self, request, *args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(CustomerUpdateView, self).dispatch(request, *args, **kwargs)
 
class CustomerDeleteView(DeleteView):
    model = customer
    success_url = reverse_lazy('order')

    def dispatch(self, request, *args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(CustomerDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

 

class ProductCreateView(CreateView):
    template_name = 'add/product_form.html'
    model = product
    fields = ['pro_name', 'au_id', 'pro_price', 'prodct_dec' ,'flag','image' ]
    
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(ProductCreateView, self).dispatch(request,*args, **kwargs)

class ProductIndexView(generic.ListView):   
    template_name = 'product.html'
    context_object_name = 'product'
    model = product
    paginate_by = 10
    def get_queryset(self):
        return product.objects.all()
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(ProductIndexView, self).dispatch(request,*args, **kwargs)

class ProductDetailView(generic.DetailView):
    model = product
    template_name = 'detail/product_detail.html'
    context_object_name = 'product'
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(ProductDetailView, self).dispatch(request,*args, **kwargs)

class ProductUpdateView(UpdateView):
    template_name = 'update/product_update.html'
    model = product
    fields = ['pro_name', 'au_id', 'pro_price', 'prodct_dec']
    success_url = reverse_lazy('product')
    
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(ProductUpdateView, self).dispatch(request,*args, **kwargs)

class ProductDeleteView(DeleteView):
    model = product
    success_url = reverse_lazy('product')
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(ProductDeleteView, self).dispatch(request,*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
  

class ComplaintIndexView(generic.ListView):
    template_name = 'complaint.html'
    context_object_name = 'complaint'
    model = complaint
    paginate_by = 10

    def get_queryset(self):
        return complaint.objects.all()
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(ComplaintIndexView, self).dispatch(request,*args, **kwargs)

class ComplaintDetailView(generic.DetailView):
    model = complaint
    template_name = 'detail/complaint_detail.html'
    context_object_name = 'complaint'
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(ComplaintDetailView, self).dispatch(request,*args, **kwargs)

class ComplaintUpdateView(UpdateView):
    template_name = 'update/complaint_update.html'
    model = complaint
    fields = ['cm_msg' , 'replay']
    success_url = reverse_lazy('complaint')
    
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(ComplaintUpdateView, self).dispatch(request,*args, **kwargs)
    
    def form_valid(self,form):
        complaint_object = complaint.objects.get(pk=self.kwargs['pk'])
        msg = form.instance.replay
        send_mail('Complaint Replay', msg , 'senseshop', [complaint_object.c_id.email])
        return super(ComplaintUpdateView, self).form_valid(form)

class ComplaintDeleteView(DeleteView):
    model = complaint
    success_url = reverse_lazy('complaint')
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(ComplaintDeleteView, self).dispatch(request,*args, **kwargs)
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
 
 

class StockCreateView(CreateView):
    template_name = 'add/stock_form.html'
    model = stock
    fields = {'pro_id','quantity','flag'}
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(StockCreateView, self).dispatch(request,*args, **kwargs)

class StockIndexView(generic.ListView):
    template_name = 'stock.html'
    context_object_name = 'stock'
    model = stock
    paginate_by = 5
    def get_queryset(self):
        return stock.objects.all()
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(StockIndexView, self).dispatch(request,*args, **kwargs)

class StockDetailView(generic.DetailView):
    model = stock
    template_name = 'detail/stock_detail.html'
    context_object_name = 'stock'
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(StockDetailView, self).dispatch(request,*args, **kwargs)

class StockUpdateView(UpdateView):
    template_name = 'update/stock_update.html'
    model = stock
    fields = {'quantity'}
    success_url = reverse_lazy('stock')
    
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(StockUpdateView, self).dispatch(request,*args, **kwargs)



class OrderIndexView(generic.ListView):
    template_name = 'orders.html'
    context_object_name = 'order'
    model = order_details
    paginate_by = 5

    def get_queryset(self):
        return order_details.objects.all()
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(OrderIndexView, self).dispatch(request,*args, **kwargs)

class OrderDetailView(generic.DetailView):
    template_name = 'detail/order_details_detail.html'
    context_object_name = 'order'
    model = order_details
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(OrderDetailView, self).dispatch(request,*args, **kwargs)

class OrderUpdateView(UpdateView):
    template_name = 'update/order_update.html'
    model = order_details
    fields = []
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(OrderUpdateView, self).dispatch(request,*args, **kwargs)

    def get_queryset(self):
        return order_details.objects.all()

class OrderDeleteView(DeleteView):
    model = order_details
    success_url = reverse_lazy('orders')

    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(OrderDeleteView, self).dispatch(request,*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class PaymentIndexView(generic.ListView):
    template_name = 'payment.html'
    context_object_name = 'payment'
    model = PayPalIPN
    paginate_by = 5

    def get_queryset(self):
        return PayPalIPN.objects.filter(flag=1)
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(PaymentIndexView, self).dispatch(request,*args, **kwargs)
 
class PaymentDetailView(generic.DetailView):
    template_name = 'detail/payment_detail.html'
    context_object_name = 'payment'
    model = PayPalIPN
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(PaymentDetailView, self).dispatch(request,*args, **kwargs)
 
    
def search(request):
    if request.method == "POST":
        query = request.POST['query']
        table = request.POST['table']
        if query:
            if table == 'product':
                product_data = product.objects.filter(pro_name__icontains=query)
                template = loader.get_template('product.html')
                context = {
                    'product':product_data, 
                }
                return HttpResponse(template.render(context,request))
            
            elif table == 'stock':
                product_data = product.objects.get(pro_name__icontains=query)
                stock_data = stock.objects.filter(pro_id=product_data.id)
                template = loader.get_template('stock.html')
                context = {
                    'stock':stock_data, 
                }
                return HttpResponse(template.render(context,request))
            elif table == 'customer':
                customer_data = customer.objects.filter(email__icontains=query)
                template = loader.get_template('customer.html')
                context = {
                    'customer':customer_data, 
                }
                return HttpResponse(template.render(context,request))
            elif table == 'transaction_id':
                payment_data = PayPalIPN.objects.filter(txn_id=query,flag=1)
                template = loader.get_template('detail/payment_detail.html')
                context = {
                    'payment':payment_data,
                }
                return HttpResponse(template.render(context,request))
            elif table == 'complaint':
                complaint_data = complaint.objects.filter(cm_msg_icontains = query)
                template = loader.get_template('detail/complaint_detail.html')
                context = {
                    'complaint':complaint_data
                }
            else:
                return redirect('index')
        else:
            return redirect('index')
    else:
            return redirect('index')
          
def logout(request):
    del request.session['myadmin']
    return redirect('index')

def handler404(request):
    response = render_to_response('404.html',{},context_instance=RequestContext(request))
    response.status_code = 404
    return response
 