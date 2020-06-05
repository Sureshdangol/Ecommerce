from .views import homeview,aboutview,registerview,loginview,contactview,kitchenview
from django.urls import path
app_name='home'

urlpatterns = [
    path('', homeview, name='home'),
    path('about',aboutview,name='about'),
    path('register',registerview,name='register'),
    path('login',loginview,name='login'),
    path('contact',contactview,name='contact'),
    path('kitchen',kitchenview,name='kitchen'),

]
