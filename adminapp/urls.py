from django.urls import *
from . import views

urlpatterns = [
    path('',views.home),
    path('asign_in_form',views.asign_in_form,name='asign_in_form'),
    path('ad_do_sign_in',views.ad_do_sign_in,name='ad_do_sign_in'),
    path('addlibraries',views.addlibraries,name='addlibraries'),
    path('savelibraries',views.savelibraries,name='savelibraries'),
    path('viewlib',views.viewlib,name='viewlib'),
    path('editlib/<int:id>',views.editlib,name='editlib'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('all_views',views.all_views,name='all_views'),
    path('delete_review/<int:id>',views.delete_review,name='delete_review'),


    
]