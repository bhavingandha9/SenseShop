from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import product,complaint,feedback,stock,order_details
from login.models import customer

def index(request):
    template = loader.get_template('admin_home.html')
    return HttpResponse(template.render(request))


class ProductCreateView(CreateView):
    template_name = 'add/product_form.html'
    model = product
    fields = ['pro_name', 'au_id', 'pro_price', 'prodct_dec' ]

class ProductIndexView(generic.ListView):
    template_name = 'product.html'
    context_object_name = 'product'
    model = product
    def get_queryset(self):
        return product.objects.all()

class ProductDetailView(generic.DetailView):
    model = product
    template_name = 'detail/product_detail.html'
    context_object_name = 'product'

class ProductUpdateView(UpdateView):
    template_name = 'update/product_update.html'
    model = product
    fields = ['pro_name', 'au_id', 'pro_price', 'prodct_dec', 'flag' ]

class ProductDeleteView(DeleteView):
    model = product
    success_url = reverse_lazy('product')




class ComplaintIndexView(generic.ListView):
    template_name = 'complaint.html'
    context_object_name = 'complaint'
    model = complaint
    def get_queryset(self):
        return complaint.objects.all()

class ComplaintDetailView(generic.DetailView):
    model = complaint
    template_name = 'detail/complaint_detail.html'
    context_object_name = 'complaint'

class ComplaintUpdateView(UpdateView):
    template_name = 'update/complaint_update.html'
    model = complaint
    fields = ['email','mobile','cm_msg','o_id','flag']


class ComplaintDeleteView(DeleteView):
    model = complaint
    success_url = reverse_lazy('complaint')


class FeedbackIndexView(generic.ListView):
    template_name = 'feedback.html'
    context_object_name = 'feedback'
    model = feedback

    def get_queryset(self):
        return feedback.objects.all()

class FeedbackDetailView(generic.DetailView):
    model = feedback
    template_name = 'detail/feedback_detail.html'
    context_object_name = 'feedback'

class FeedbackUpdateView(UpdateView):
    template_name = 'update/feedback_update.html'
    model = feedback
    fields = ['email', 'mobile', 'f_msg', 'flag']


class FeedbackDeleteView(DeleteView):
    model = feedback
    success_url = reverse_lazy('feedback')


class StockCreateView(CreateView):
    template_name = 'add/stock_form.html'
    model = stock
    fields = {'pro_id','quantity'}

class StockIndexView(generic.ListView):
    template_name = 'stock.html'
    context_object_name = 'stock'
    model = stock

    def get_queryset(self):
        return stock.objects.all()

class StockDetailView(generic.DetailView):
    model = stock
    template_name = 'detail/stock_detail.html'
    context_object_name = 'stock'

class StockUpdateView(UpdateView):
    template_name = 'update/stock_update.html'
    model = feedback
    fields = {'pro_id','quantity'}




class OrderIndexView(generic.ListView):
    template_name = 'order_details.html'
    context_object_name = 'order'
    model = order_details
    def get_queryset(self):
        return order_details.objects.all()

class OrderDetailView(generic.DetailView):
    template_name = 'detail/order_details_detail.html'
    context_object_name = 'order'
    model = order_details

class OrderUpdateView(UpdateView):
    template_name = 'update/complaint_update.html'
    model = order_details
    fields = ['email','mobile','cm_msg','o_id']

class OrderDeleteView(DeleteView):
    model = order_details
    success_url = reverse_lazy('order')

class CustomerCreateView(generic.CreateView):
    template_name = 'add/customer_form.html'
    model = customer
    fields = {}

class CustomerIndexView(generic.ListView):
    template_name = 'customer.html'
    context_object_name = 'customer'
    model = customer
    def get_queryset(self):
        return customer.objects.all()

class CustomerDetailView(generic.DetailView):
    template_name = 'detail/customer_detail.html'
    context_object_name = 'order'
    model = customer

class CustomerUpdateView(UpdateView):
    template_name = 'update/_update.html'
    model = customer
    fields = ['email','mobile']

class CustomerDeleteView(DeleteView):
    model = customer
    success_url = reverse_lazy('order')

def logout(request):
    del request.session['myadmin']
    return redirect('index')