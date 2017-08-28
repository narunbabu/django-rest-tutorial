from django.conf.urls import url
from gnippets import views

urlpatterns = [
    url(r'^gnippets/$', views.gnippet_list),
    url(r'^gnippets/(?P<pk>[0-9]+)/$', views.gnippet_detail),
]