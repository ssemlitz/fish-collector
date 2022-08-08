from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish, Feeding
from .forms import FeedingForm

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
  feeding_form = FeedingForm()
  return render(request, 'fishies/detail.html', { 'fish': fish, 'feeding_form': feeding_form })

class FishCreate(CreateView):
  model = Fish
  fields = '__all__'

class FishUpdate(UpdateView):
  model = Fish
  fields = '__all__'

class FishDelete(DeleteView):
  model = Fish
  success_url = '/fishies/'

def add_feeding(request, fish_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.fish_id = fish_id
    new_feeding.save()
  return redirect('fishies_detail', fish_id=fish_id)

