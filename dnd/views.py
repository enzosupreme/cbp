from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import NonPlayerCharacter, Affiliation, Character_Sheet,Skill_Class, Weapon, Skill, Race

from .forms import NewCharacterForm


def detail(request, pk):
    npcs = get_object_or_404(NonPlayerCharacter, pk=pk)



    return render(request, 'dnd/detail.html', {
        'npcs': npcs,

    })
def NPC(request):
    #query = request.Get.get('query', npcs.affiliation)
    #affiliation_id = request.GET('affiliation', 0)
    npcs = NonPlayerCharacter.objects.filter(invisible=False)
    affiliation = Affiliation.objects.all()

    #if category_id:
        #projects = projects.filter(category_id=category_id)
    #if query:
        #projects = projects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'dnd/npcs.html', {
        'npcs': npcs,
        #'query':query,
        'affiliation':affiliation,
        #'affiliation_id': int(affiliation_id)
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewCharacterForm(request.POST, request.FILES)

        if form.is_valid():
            npcs = form.save(commit=False)
            npcs.created_by = request.user
            npcs.save()

            return redirect('dnd:npcs')

    else:
        form = NewCharacterForm()

    return render(request, 'dnd/form.html', {
        'form': form,
        'title': 'New Character'
    })


def Character(request):

    characters = Character_Sheet.objects.filter(invisible=False)
    skill_class = Skill_Class.objects.all()
    skill = Skill.objects.all()
    race = Race.objects.all()
    weapon = Weapon.objects.all()

    return render(request, 'dnd/characters.html', {
        'characters':characters,
        'skill_class':skill_class,
        'skill':skill,
        'race':race,
        'weapon':weapon,
    })

def character_detail(request, pk):
    characters = get_object_or_404(Character_Sheet, pk=pk)


    return render(request, 'dnd/character_detail.html', {
        'characters': characters,

    })