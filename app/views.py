from django.shortcuts import render
from .models import CustomUser
from django.db.models import Avg,Min,Max

def home(request):
    # todos = CustomUser.objects.filter(pk_id = 5)
    context = CustomUser.objects.aggregate(avg_age = Avg('age'),max_age = Max('age'),min_age = Min('age'))
    userFilter = CustomUser.objects.filter(age = 18)
    context['userFilter'] = userFilter
    return render(request, 'home.html', context)

