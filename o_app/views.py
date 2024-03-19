from django.shortcuts import render,HttpResponse
from django.http import QueryDict
from o_app.models import Contact
# Create your views here.

def index(request):
    return render(request, 'index.html')

def service(request):
    data = {
        "name" : "wazie",
        "l_name" : "Shaikh",
        "subject":['python','c#',"Java",'JavaScript'],
        
        'stu_cont' : [
            {
            'name':"waize", 
            'email':'waize@gmail.com','phone':'3189402688'
            },
            
            {
            'name':"zohaib", 
            'email':'zohaib@gmail.com','phone':'3133876980'
            }
        ],
        
        'num' : [1,23,45,67,78,79,80,78]
    }
    return render(request, 'service.html',data)

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        contact = Contact(email=email,password=password)
        contact.save()
        print("Success save")
    return render(request, 'contact.html')
