from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Fish
from .forms import FeedingForm

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def fishies_index(request):
  fishies = Fish.objects.filter(user=request.user)
  return render(request, 'fishies/index.html', { 'fishies': fishies })

@login_required
def fishies_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  feeding_form = FeedingForm()
  return render(request, 'fishies/detail.html', { 'fish': fish, 'feeding_form': feeding_form })

class FishCreate(LoginRequiredMixin, CreateView):
  model = Fish
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class FishUpdate(LoginRequiredMixin, UpdateView):
  model = Fish
  fields = '__all__'

class FishDelete(LoginRequiredMixin, DeleteView):
  model = Fish
  success_url = '/fishies/'

@login_required
def add_feeding(request, fish_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.fish_id = fish_id
    new_feeding.save()
  return redirect('fishies_detail', fish_id=fish_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)