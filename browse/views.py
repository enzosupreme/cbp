
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from projects.models import Project, Category, About, Garden_Pic


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