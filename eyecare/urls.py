from django.urls import path
from eyecare import views
urlpatterns = [
    path('',views.index,name="index") ,
    path('login1',views.login1,name="login1"),
    path('main',views.main,name="main"),
    path('search',views.search,name="search"),
    path('appoints',views.appoints,name="appoints")
]
