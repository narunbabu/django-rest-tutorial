from django.conf.urls import url
from dinosaurs import views

urlpatterns = [
    url(r'^dinosaurs/$', views.dinosaurs_list),
    url(r'^dinosaurs/(?P<pk>[0-9]+)/$', views.dinosaur_detail),
    url(r'^dinosaurs/(?P<teeth>[0-9]+)/$', views.dinosaur_detail),

]