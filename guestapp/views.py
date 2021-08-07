from django.shortcuts import render
from adminapp. models import Library,Reviews

# Create your views here.


def write_review(request,id):

    lib = Library.objects.get(id=id)
    return render(request, 'writeview.html',{'lib':lib})


def save_review(request,id):

    lib = Library.objects.get(id=id) 
    name =  request.POST['name']   
    review = request.POST['review']
    val=Reviews(LibName=lib.Name, Name=name,  Reviews=review)
    val.save()
    lib = Library.objects.all()
    return render(request, 'home.html',{'lib':lib})





