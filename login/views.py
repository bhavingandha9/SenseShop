from django.shortcuts import render
from .models import customer
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

def index(request):
    if request.session.has_key('user'):
        return redirect('user')
    else:
        all_customer = customer.objects.all()
        template = loader.get_template('login/index.html')
        context = {'all_customer': all_customer,}
        return HttpResponse(template.render(context,request))

def login_check(request):

    form_user= request.POST['email']
    form_passowrd= request.POST['password']
    all_users = customer.objects.all()

    for users in all_users:
        if users.email in form_user and users.password in form_passowrd and users.cflag == 1:
            flag = 1
            break
        elif users.email in form_user and users.password in form_passowrd and users.cflag == 2:
            flag = 2
            break
        else:
            flag = 0

    if flag == 1:
        request.session['user'] = form_user
        return redirect('user')
    elif flag == 2:
        request.session['myadmin'] = form_user
        return redirect('myadmin')
    else:
        return redirect('index')

