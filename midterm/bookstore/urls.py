from django.conf.urls import url

from . import views

app_name = 'bookstore'

urlpatterns = [
    url(r'^$', views.index, name='bookstore'),
    url(r'^listbook/$',views.listbook, name='listbook'),
    url(r'^insertbook/$',views.insertbook,name='insertbook'),
    url(r'^listbook/update/$',views.update),
    url(r'^listbook/delete/$',views.delete),
]
