from . import views
from django.urls import path

urlpatterns = [

    path('detail',views.detail,name='detail')
]