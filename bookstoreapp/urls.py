from . import views
from django.urls import path
app_name='bookstoreapp'
urlpatterns = [

    path('',views.demo,name='demo')
]