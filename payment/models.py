from django.db import models
from paypal.standard.ipn.signals import payment_was_successful

def show_me_the_money(sender, **kwargs):
    code = sender.item_number
    type, number_product, pagamento_corso_id = code.split('_')
    obj = get_object_or_404(PagamentoCorso, int(pagamento_corso_id))
    obj.pagamento = True
    obj.save()

payment_was_successful.connect(show_me_the_money)