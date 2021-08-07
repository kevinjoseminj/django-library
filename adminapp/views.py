from django.shortcuts import render,redirect
from . models import Administrator,Library,Reviews


# Create your views here.

def home(request):
    lib = Library.objects.all()
    return render(request, 'home.html',{'lib':lib})
    return render(request,'home.html')


def asign_in_form(request):
    return render(request, 'asign.html')


def ad_do_sign_in(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        result = Administrator.objects.all()
        for x in result:
            if email in x.Email:
                if password in x.Password:
                    print(x.Password)
                    library = Library.objects.all()
                    return render(request, 'adminhome.html',{'library':library})  
                else:
                    return render(request, 'asign.html',{'m':'Wrong password'})
            else:
                return render(request, 'asign.html',{'m':'Wrong Username'})
    except Exception as e:
        return render(request, 'asign.html', {'m': 'An error occured'})



def libraries(request):
    return render(request, 'libraries.html')


def addlibraries(request):
    return render(request,'addlib.html')


def savelibraries(request):
    liname = request.POST['liname']
    liaddress = request.POST['liaddress']
    licity = request.POST['licity']    
    val=Library(Name=liname, Address=liaddress, City=licity)
    val.save()
    library = Library.objects.all()
    return render(request,'adminhome.html',{'library':library})


def viewlib(request):
    lib = Library.objects.all()
    return render(request,'adminhome.html',{'lib':lib})


def editlib(request,id):
    lib = Library.objects.get(id=id)
    return render(request, 'editlib.html',{'lib':lib})


def update(request,id):
    lib = Library.objects.get(id=id)
    liname = request.POST['liname']
    liaddress = request.POST['liaddress']
    licity = request.POST['licity']
    Library.objects.filter(pk=id).update(Name=liname, Address=liaddress, City=licity)
    library = Library.objects.all()
    return render(request,'adminhome.html',{'library':library})


def delete(request,id):
    lib = Library.objects.get(id=id)
    lib.delete()
    library = Library.objects.all()
    return render(request,'adminhome.html',{'library':library})
    

def all_views(request):
    val = Reviews.objects.all()
    return render(request,'allreview.html',{'val':val})

def delete_review(request,id):
    
    re = Reviews.objects.get(id=id)
    re.delete()
    val = Reviews.objects.all()
    return render(request,'allreview.html',{'val':val})


