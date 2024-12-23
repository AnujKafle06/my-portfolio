from django.shortcuts import render
from. models import Skill

# Create your views here.
def home(request): 
    first = Skill.objects.filter(pk__in=[1, 2, 3])
    second = Skill.objects.filter (pk__in=[4, 5, 6])

    context={
        first : 'first',
        second : 'second'

    }
    fetch= Skill.objects.all()

    return render(request, 'index.html', {'fetch':fetch})