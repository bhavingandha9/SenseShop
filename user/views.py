from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.shortcuts import redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from myadmin.models import product,order_details,complaint,feedback

class OrderIndexView(generic.ListView):

    template_name = 'user_home.html'
    context_object_name = 'order'
    model = order_details

    def get_queryset(self):

       return order_details.objects.all()


class OrderDetailView(generic.DetailView):
    model = order_details
    template_name = 'user_home.html'

class ComplaintCreateView(CreateView):
    template_name = 'add/complaint_form.html'
    model = complaint
    fields = ['email','mobile','cm_msg','o_id','flag']

class FeedbackCreateView(CreateView):
        template_name = 'add/feedback_form.html'
        model = feedback
        fields = ['email', 'mobile', 'f_msg', 'flag']

def logout(request):
            del request.session['user']
            return redirect('index')

#def hello(request):
  #  template = loader.get_template('user_home.html')
  #  return HttpResponse(template.render(request))
    #html = "u r in a diff app"
    #return HttpResponse(html)