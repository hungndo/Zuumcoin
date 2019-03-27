from django.conf.urls import url
from . import views


app_name='zuumcoin'
urlpatterns = [
    url(r'', views.user_interface, name='interface'),
    url(r'swicht', views.switch, name='switch')
]