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

class Adminhome(generic.ListView):
    template_name = 'admin_home.html'
    model = product
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(Adminhome, self).dispatch(request,*args, **kwargs)

    def get_queryset(self):
        return product.objects.all()


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
    fields = ['email', 'mobile']

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
    fields = ['pro_name', 'au_id', 'pro_price', 'prodct_dec' ,'flag' ]

class ProductIndexView(generic.ListView):
    template_name = 'product.html'
    context_object_name = 'product'
    model = product
    paginate_by = 5
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
    fields = ['pro_name', 'au_id', 'pro_price', 'prodct_dec', 'flag' ]
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
    paginate_by = 2

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
    fields = ['email','mobile','cm_msg','o_id']
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(ComplaintUpdateView, self).dispatch(request,*args, **kwargs)

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
 

class FeedbackIndexView(generic.ListView):
    template_name = 'feedback.html'
    context_object_name = 'feedback'
    model = feedback
    paginate_by = 5

    def get_queryset(self):
        return feedback.objects.all()
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(FeedbackIndexView, self).dispatch(request,*args, **kwargs)

class FeedbackDetailView(generic.DetailView):
    model = feedback
    template_name = 'detail/feedback_detail.html'
    context_object_name = 'feedback'
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(FeedbackDetailView, self).dispatch(request,*args, **kwargs)

class FeedbackUpdateView(UpdateView):
    template_name = 'update/feedback_update.html'
    model = feedback
    fields = ['email', 'mobile', 'f_msg', 'flag']
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(FeedbackUpdateView, self).dispatch(request,*args, **kwargs)

class FeedbackDeleteView(DeleteView):
    model = feedback
    success_url = reverse_lazy('feedback')
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(FeedbackDeleteView, self).dispatch(request,*args, **kwargs)
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
 

class StockCreateView(CreateView):
    template_name = 'add/stock_form.html'
    model = stock
    fields = {'pro_id','quantity'}
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
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(StockUpdateView, self).dispatch(request,*args, **kwargs)



class OrderIndexView(generic.ListView):
    template_name = 'order_details.html'
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
    success_url = reverse_lazy('order')
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('myadmin'):
            a = 'hello'
        else:
            return redirect('index')
        return super(OrderDeleteView, self).dispatch(request,*args, **kwargs)





def logout(request):
    del request.session['myadmin']
    return redirect('index')