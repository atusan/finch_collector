from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.http import HttpResponse
from .models import Art, Location
from .forms import FeedingForm

# class Art:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, type, date):
#     self.name = name
#     self.type = type
#     self.date = date
   

# arts = [
#   Art('The Kiss', 'watercolor', 1907),
#   Art('Mona Lisa', 'watercolor', 1665),
#   Art('Girl with a Pearl Earring','watercolor', 1665),
# ]

# Create your views here.
class ArtCreate(CreateView):
      model = Art
      fields = '__all__'

class ArtUpdate(UpdateView):
      model = Art
  # Let's disallow the renaming of a cat by excluding the name field!
      fields = ['name', 'type', 'date']

class ArtDelete(DeleteView):
      model = Art
      success_url = '/arts/'


def home(request):
      # return HttpResponse('<h1>Hello homepage</h1>')
      return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def arts_index(request):
      arts = Art.objects.all()
      return render(request, 'arts/index.html', { 'arts': arts })

def arts_detail(request, art_id):
      art = Art.objects.get(id=art_id)
      # test = Location.objects.filter(id__in = art.locations.all().values_list('id'))
      toys_cat_doesnt_have = Location.objects.exclude(id__in = art.locations.all().values_list('id'))
      feeding_form = FeedingForm()
      return render(request, 'arts/detail.html', { 'art': art ,'feeding_form': feeding_form, 'locations': toys_cat_doesnt_have})

def assoc_location(request, art_id, location_id):
      # Note that you can pass a toy's id instead of the whole object
      Art.objects.get(id=art_id).locations.add(location_id)
      return redirect('detail', art_id=art_id)

def add_feeding(request, art_id):
      # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.art_id = art_id
    new_feeding.save()
  return redirect('detail', art_id=art_id)

  
    
