from django.conf.urls import url
from django.contrib import admin
from login import views
from user import views as a
from myadmin import views as b

urlpatterns = [
    url(r'^$',views.index, name='index'),

    url(r'^login_check/$', views.login_check,name='login_check'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^forgot_password/',views.send, name='forgot_password'),

    url(r'^myadmin/$', b.index, name='myadmin'),
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
 
    url(r'^myadmin/customer', b.CustomerIndexView.as_view(), name='customer'),
    url(r'^myadmin/customer/(?P<pk>[0-9]+)/$', b.CustomerDetailView.as_view(), name='customer_detail'),
    url(r'^myadmin/customer/add$', b.CustomerCreateView.as_view(), name='customer_add'),
    url(r'^myadmin/customer/delete/(?P<pk>[0-9]+)/$', b.CustomerUpdateView.as_view(), name='customer_delete'),
    url(r'^myadmin/customer/update/(?P<pk>[0-9]+)/$', b.CustomerDeleteView.as_view(), name='customer_update'),
    
    url(r'^myadmin/payments', b.PaymentsIndexView.as_view(), name='payments'),

    url(r'^myadmin/orders$',b.OrderIndexView.as_view(),name='orders'),
    
    url(r'^myadmin/search',b.search , name='myadmin_search'),

    url(r'^myadmin_logout/', b.logout, name='myadmin_logout'),

    url(r'^user/$',a.OrderIndexView.as_view(), name='user'),
    url(r'^user/complaint$',a.ComplaintCreateView.as_view(), name='complaintadd'),
    
    url(r'^user_logout/', a.logout, name='user_logout'),
]