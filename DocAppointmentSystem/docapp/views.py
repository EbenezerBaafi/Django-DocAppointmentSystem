from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_subject = request.POST['message-subject']
        yourmessage = request.POST['yourmessage']
        message_email = request.POST['message-email']

        send_mail(
            message_name,
            message_email,
            yourmessage,
            message_subject,
            ['ebaafi007@gmail.com']
        )

        return render(request, 'contact.html', {'message-name': message_name})
    else:
        return render(request, 'contact.html', {})
    
def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request, 'services.html', {})

def doctors(request):
    return render(request, 'doctors.html', {})
def blog(request):
    return render(request, 'blog.html', {})
def appointment(request):
    return render(request, 'appointment.html', {})
def single(request):
    return render(request, 'single.html', {})
def elements(request):
    return render(request, 'elements.html', {})
