from django.conf.urls import url
from .api import LoginView, LogoutView

urlpatterns = [
    url(r'^login/$', LoginView.as_view()),  #becaoz our views are classes, not methods, Therefore we have to use as_View method
    url(r'^logout/$', LogoutView.as_view())
]