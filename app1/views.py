from django.shortcuts import render, redirect
from .forms import FlickForm
from app1.models import Flick


def index(request):
    if request.method == 'POST':
        form = FlickForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        flicks = Flick.objects.all()
        form = FlickForm()
    return render(request, 'app1/index.html', {'form': form,'flicks':flicks})

