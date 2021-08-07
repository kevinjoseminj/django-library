from django.urls import *
from . import views

urlpatterns = [
    path('view_reviews/<int:id>',views.view_reviews,name='view_reviews'),   
]