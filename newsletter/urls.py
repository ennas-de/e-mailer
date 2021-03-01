from django.urls import path
from . import views

app_name = 'newsletter'

# add urlpatterns
urlpatterns = [
    path('', views.register, name='register'),
    path('test', views.test, name='test'),

]
