from django.conf.urls import url
from first_app import views

urlpatterns = [

    url(r'^$Page1',views.index,name='index'),
    ]
