from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Add the Cat class & list and view function below the imports
class Fish:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

fishies = [
  Fish('Lolo', 'tabby', 'Kinda rude.', 3),
  Fish('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Fish('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Fish('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

def home(request):
  return HttpResponse('<h1>FISHIES</h1>')

def about(request):
  return render(request, 'about.html')

def fishies_index(request):
  return render(request, 'fishies/index.html', {'fishies':fishies})