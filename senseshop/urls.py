from django.conf.urls import url,handler404,include
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import admin
from login import views
from user import views as a
from myadmin import views as b 

handler404 = b.handler404
 
urlpatterns = [
    url('', include('pwa.urls')),
    url(r'^$',views.index, name='index'),

    url(r'^login_check/$', views.login_check,name='login_check'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^forgot_password/',views.send, name='forgot_password'),

    url(r'^myadmin/$', b.ProductIndexView.as_view(), name='myadmin'),
    url(r'^myadmin/product/$',b.ProductIndexView.as_view(),name='product'),
    url(r'^myadmin/product/(?P<pk>[0-9]+)/$',b.ProductDetailView.as_view(),name='product_detail'),
    url(r'^myadmin/product/add$', b.ProductCreateView.as_view(), name='product_add'),
    url(r'^myadmin/product/update/(?P<pk>[0-9]+)/$', b.ProductUpdateView.as_view(), name='product_update'),
    url(r'^myadmin/product/delete/(?P<pk>[0-9]+)/$', b.ProductDeleteView.as_view(), name='product_delete'),

    url(r'^myadmin/complaint$',b.ComplaintIndexView.as_view(),name='complaint'),
    url(r'^myadmin/complaint/(?P<pk>[0-9]+)/$', b.ComplaintDetailView.as_view(), name='complaint_detail'),
    url(r'^myadmin/complaint/update/(?P<pk>[0-9]+)/$', b.ComplaintUpdateView.as_view(), name='complaint_update'),
    url(r'^myadmin/complaint/delete/(?P<pk>[0-9]+)/$', b.ComplaintDeleteView.as_view(), name='complaint_delete'),
   
    url(r'^myadmin/stock/add$',b.StockCreateView.as_view(),name='stock_add'),
    url(r'^myadmin/stock$', b.StockIndexView.as_view(), name='stock'),
    url(r'^myadmin/stock/(?P<pk>[0-9]+)/$', b.StockDetailView.as_view(), name='stock_detail'),
    url(r'^myadmin/stock/update/(?P<pk>[0-9]+)/$', b.StockUpdateView.as_view(), name='stock_update'),
 
    url(r'^myadmin/customer$', b.CustomerIndexView.as_view(), name='customer'),
    url(r'^myadmin/customer/(?P<pk>[0-9]+)/$', b.CustomerDetailView.as_view(), name='customer_detail'),
    url(r'^myadmin/customer/add$', b.CustomerCreateView.as_view(), name='customer_add'),
    url(r'^myadmin/customer/delete/(?P<pk>[0-9]+)/$', b.CustomerDeleteView.as_view(), name='customer_delete'),
    url(r'^myadmin/customer/update/(?P<pk>[0-9]+)/$', b.CustomerUpdateView.as_view(), name='customer_update'),
    
    url(r'^myadmin/payment$', b.PaymentIndexView.as_view(), name='payment'),
    url(r'^myadmin/payment/(?P<pk>[0-9]+)/$', b.PaymentDetailView.as_view(), name='payment_detail'),

    url(r'^myadmin/orders$',b.OrderIndexView.as_view(),name='orders'),
    url(r'^myadmin/orders/(?P<pk>[0-9]+)/$', b.OrderDetailView.as_view(), name='orders_detail'),
    url(r'^myadmin/orders/delete/(?P<pk>[0-9]+)/$', b.OrderDeleteView.as_view(), name='order_delete'),
    
    
    url(r'^myadmin/search',b.search , name='myadmin_search'),

    url(r'^myadmin_logout/', b.logout, name='myadmin_logout'),

    url(r'^user/$',a.Userhome.as_view(), name='user'),
    url(r'^user/complaint$',a.complaint_form, name='user_complaint'),
    url(r'^user/complaint/add$',a.ComplaintCreate,name='complaintadd'),
    url(r'^user/order$',a.OrderIndexView.as_view(), name='user_order'),
    url(r'^user/order_detail/(?P<pk>[0-9]+)/$', a.OrderDetailView.as_view(), name='user_order_details'),
    url(r'^user/add2cart$', a.add2cart, name='add2cart'),    
    url(r'^user_logout/', a.logout, name='user_logout'),
    url(r'^user/cart$', a.Cart.as_view(), name='cart'),
    url(r'^user/quantity_inc$', a.quantity_inc, name='quantity_inc'),
    url(r'^user/quantity_dec$', a.quantity_dec, name='quantity_dec'),
    url(r'^user/remove_product$', a.remove_product, name='remove_product'),
    url(r'^user/checkout$', a.checkout, name='checkout'),
    url(r'^user/payment$', a.payment, name='user_payment'),    
    url(r'^user/search',a.search , name='user_search'),
    url(r'^paypal/',include('paypal.standard.ipn.urls')),
    url(r'^payment/',include('payment.urls', namespace = 'payment')),
    
    
    
    
    url('^serviceworker.js$', a.service_worker),
    url('^manifest.json$', a.manifest,name ='manifest.json'),
    url('', include('pwa.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]