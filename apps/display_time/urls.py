from django.conf.urls import url
from . import views             # This line is new!
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
]