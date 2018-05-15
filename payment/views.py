from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import HttpResponse


@csrf_exempt
def payment_done(request):
    return redirect('checkout')

@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')

def payment_process(request):
    amount = request.session['amount']
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': amount,
        'item_name': 'abc',
        'currency_code': 'INR',
        'notify_url': 'http://senseshop.tk{}'.format(reverse('paypal-ipn')),
        'return_url': 'http://senseshop.tk{}'.format(reverse('payment:done')),
        'cancel_url': 'http://senseshop.tk{}'.format(reverse('payment:canceled')),
    }
    form = PayPalPaymentsForm(initial = paypal_dict)
    return render(request,'payment/process.html',{'form': form })