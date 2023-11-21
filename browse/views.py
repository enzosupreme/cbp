
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
#from adafruit_IO import Client,MQTTClient,Feed
from .models import Santa, Gift
from .forms import SignupForm
import random
from projects.models import Project, Category, About, Garden_Pic

#username = 'your_adafruit_io_username'
#key = 'your_adafruit_io_key'

#aio = adafruitIO(username, key)
#feed_id = feed['thermo']

def index(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    projects = Project.objects.filter(invisible=False)
    categories = Category.objects.all()

    if category_id:
        projects = projects.filter(category_id=category_id)
    if query:
        projects = projects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'browse/index.html', {
        'projects': projects,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })

def projects(request):
    query = request.GET.get('query', projects.category)
    category_id = request.GET('category', 0)
    projects = Project.object.filter(invisible=False)
    categories = Category.objects.all()

    if category_id:
        projects = projects.filter(category_id=category_id)

    if query:
        projects = projects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'browse/index.html', {
        'projects': projects,
        'query':query,
        'categories':categories,
        'category_id': int(category_id)
    })
def garden(request):
    images = Garden_Pic.objects.all()

    return render(request, 'browse/shangri-la.html', {
        'images':images,
    })

def image(request, pk):
    images = get_object_or_404(Garden_Pic, pk=pk)

    return render(request, 'browse/images.html', {
        'images': images,
    })
@login_required
def thermo(request):

    return render(request, 'browse/thermo.html', {
        #'images':images,
    })

def santa(request):
    santas = Santa.objects.all()
    r = random.randint(0,(len(santas)-1))

    secret_santa = santas[r]

    return render(request, 'browse/santa.html', {
        'r': r,
        'santas': santas,
        'secret_santa': secret_santa
    })

def signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'browse/signup.html', {

        'form': form
    })

def gift(request):

    gifts = Gift.objects.all()

    return render(request,'browse/santa.html', {
        'gifts': gifts
    })


