from django.urls import *
from . import views

urlpatterns = [
    path('write_review/<int:id>',views.write_review,name='write_review'),
    path('save_review/<int:id>',views.save_review,name='save_review'),    
]