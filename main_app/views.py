from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def fishies_index(request):
  fishies = Fish.objects.all()
  return render(request, 'fishies/index.html', { 'fishies': fishies })

def fishies_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  return render(request, 'fishies/detail.html', { 'fish': fish })

class FishCreate(CreateView):
  model = Fish
  fields = '__all__'

class FishUpdate(UpdateView):
  model = Fish
  fields = '__all__'

class FishDelete(DeleteView):
  model = Fish
  success_url = '/fishies/'

