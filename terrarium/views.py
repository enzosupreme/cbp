from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant,Terrarium



def plants(request):
    plants = Plant.objects.all()

    return render(request, 'terrarium/plants.html', {
        'plants': plants,

    })

def terrariums(request):
    terrariums = Terrarium.objects.all()

    return render(request, 'terrarium/terrarium.html', {
        'terrariums': terrariums
    })

def detail(request, pk):
    habitats = get_object_or_404(Terrarium, pk=pk)

    return render(request, 'terrarium/detail.html', {
        'habitats': habitats,

    })

def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)

    return render(request, 'terrarium/plant_detail.html', {
        'plant': plant,

    })