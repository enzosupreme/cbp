from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

from projects.models import Category, Project, Service, ServiceRequest, Menu_item, About

from .forms import ServiceForm

def index(request):
    projects = Project.objects.filter(front_page=True)[0:2]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'projects': projects,
    })

def commission(request):
    services = Service.objects.all()


    return render(request, 'core/commission.html', {
        'services': services
    })
def menu_items(request):
    menu_items = Menu_item.objects.all()


    return render(request, 'core/menu.html', {
        'menu_items': menu_items
    })
def services(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            html = render_to_string('core/servicerequest.html',{
                'email' : email,
                'message': message,
                'subject': subject
            })
            send_mail(subject,message,email,['circuitboredlab@gmail.com'],html_message=html)
            return redirect('/')
        else:
            print('is not valid')
            form = ServiceForm()
        message_subject = request.POST['message-subject']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            subject,# subject
            message, #message
            message_email, #from email
            ['circuitboredlab@gmail.com'], #To email
        )
    form = ServiceForm()

    return render(request, 'core/services.html',{
        'form':form,
    })

def about(request):
    about = About.objects.all()

    return render(request, 'core/about.html', {
        'about':about
    })
