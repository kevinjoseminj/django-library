from django.shortcuts import render
from adminapp. models import Library,Reviews


# Create your views here.


def view_reviews(request,id):
    
    re = Reviews.objects.all()
    return render(request,'reviewlist.html',{'re':re})






