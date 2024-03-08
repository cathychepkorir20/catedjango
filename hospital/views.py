from django.shortcuts import render,redirect

from hospital.forms import ImageUploadForm
from hospital.models import Member, Appointment, Users, Products, ImageModel


# Create your views here.
def index(request):
    if request.method == 'POST':
        appointment = Appointment(name=request.POST['name'],
                                  email=request.POST['email'],
                                  phone=request.POST['phone'],
                                  date=request.POST['date'],
                                  department=request.POST['department'],
                                  doctor=request.POST['doctor'],
                                  message=request.POST['message'])
        appointment.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def register(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], email=request.POST['email'],
                        password=request.POST['password'])
        member.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')


def login(request):
     return render(request, 'login.html')


def appointmentdetails(request):
    myappoint = Appointment.objects.all
    return render(request, 'appointmentdetails.html', {'myappoint': myappoint})


def users(request):
    myusers = Users.objects.all()
    return render(request, 'user.html', {'myusers': myusers})


def products(request):
    myproducts = Products.objects.all()
    return render(request, 'products.html', {"myproducts": myproducts})


def adminhome(request):
    if request.method == "POST":
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'],
                                        password=request.POST['password'])
            return render(request, 'adminhome.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'showimages.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')