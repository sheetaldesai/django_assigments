from django.conf.urls import url
from . import views             # This line is new!
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^new/$', views.new),
    url(r'^create/$',views.create),
    url(r'(?P<num>[0-9]+)/$',views.show),
    url(r'(?P<num>[0-9]+)/edit/$',views.edit),
    url(r'(?P<num>[0-9]+)/destroy/$',views.destroy)
]