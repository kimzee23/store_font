from django.shortcuts import redirect
from django.urls import path,include


from . import views, admin

#my url config
urlpatterns = [

    path('',views.something),

]