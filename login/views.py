from django.shortcuts import render
from .models import customer
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings

def index(request):

    if request.session.has_key('user'):
        return redirect('user')
    elif request.session.has_key('myadmin'):
        return redirect('myadmin')
        #return HttpResponse(request.session['user'])
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
        request.session.modified = True
        
        return redirect('user')
    elif flag == 2:
        request.session['myadmin'] = form_user
        request.session.modified = True

        return redirect('myadmin')
    else:
        return redirect('index')


def send(request):
    if request.method == "POST":
        email = request.POST['forgot_email']
        all_users = customer.objects.all()
        result = 'hello'
        for users in all_users:
            if users.email in email:
                send_mail('PasswordReset', users.password , 'senseshop', [users.email])
                return redirect('/?message=success')

        return redirect('/?message=failed')
