from django.shortcuts import render, redirect, HttpResponse
from .models import Video,VideoModels
from .forms import Video_form
import razorpay
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    videos = Video.objects.all()
    print(videos)
    return render(request,'admins/home.html',{'videos':videos})

def index(request):
    return render(request,'index.html')


def add_video(request):
        all_videos =Video.objects.all()
        if request.method == 'POST':
            form = Video_form(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                alert = True
                return HttpResponse("<h1> Uploaded successfully</h1>")
        else:
                form = Video_form()
        return render(request, 'admins/add_video.html', {'form': form, 'all_videos': all_videos})

def view_video(request):
    videos = Video.objects.all()
    videos_all = VideoModels.objects.filter(videos=videos)

    context = {'videos': videos, 'videos_all': videos_all}
    return render(request, "view_video.html",context)


def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        image = request.FILES['image']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "admins/registration.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        #student = Student.objects.create(user=user, phone=phone,image=image)
        user.save()
        #student.save()
        alert = True
        return render(request, "admins/login.html", {'alert':alert})
    return render(request, "admins/registration.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('add_video')
            elif user.is_active:
                return redirect('home')
        else:
            alert = True
            return render(request, "admins/login.html", {'alert':alert})
    return render(request, "admins/login.html")

def Logout(request):
    logout(request)
    return redirect ("home")

# from django.conf import settings
# def buy(request):
#     buy_obj = Video.objects.get(is_paid=False , user=request.user)
#     if request.method=='POST':
#         client =razorpay.Client(auth = (settings.razor_pay_key_id , settings.key_secret))
        


