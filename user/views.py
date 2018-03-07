from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.shortcuts import redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from myadmin.models import product,order_details,complaint 
from django.core.urlresolvers import reverse_lazy


class OrderIndexView(generic.ListView): 
    template_name = 'user_home.html'
    context_object_name = 'order'
    model = order_details

    def get_queryset(self): 
       return order_details.objects.all()
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

class ComplaintCreateView(CreateView):
    template_name = 'add/complaint_form.html'
    model = complaint
    fields = ['c_id','cm_msg','o_id','replay','flag']
    success_url = reverse_lazy('myadmin')
    def dispatch(self,request ,*args, **kwargs):
        if request.session.has_key('user'):
            a = 'hello'
        else:
            return redirect('index')
        return super(ComplaintCreateView, self).dispatch(request,*args, **kwargs)
        
def logout(request):
            del request.session['user']
            return redirect('index')

#def hello(request):
  #  template = loader.get_template('user_home.html')
  #  return HttpResponse(template.render(request))
    #html = "u r in a diff app"
    #return HttpResponse(html)