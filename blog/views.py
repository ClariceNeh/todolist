from django.shortcuts import render
from dev.models import Useradmin

def home(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})



def contact(request):
    # name='good morning'
    # return render(request, 'contact.html',{'username':name})
    if request.method =="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        password= request.POST.get('password')
        image= request.POST.get('image')


        user = Useradmin.objects.create(name=name,email=email,password=password, image=image)
        if user:
             return render(request, 'tech.html')    
            # print("user is created")
        else:
            print('refuse')
    return render(request, 'contact.html')
def tech(request):
    return render(request, 'tech.html')    
def employ(request):
    user=Useradmin.objects.all()
    context={'user':user}

    return render(request, 'employ.html',context)    