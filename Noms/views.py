from django.shortcuts import render, get_object_or_404

from .forms import NomForm


from .models import Food_model

# Create your views here.
def index(request):
    #context = {""}
    return render(request, "Noms/index.html")

def nom(request):
    if request.method == 'POST':
        foodform = NomForm(request.POST)
        if foodform.is_valid():
            return render(request, "Noms/index.html")
    else:
        foodform = NomForm
    
    return render(request, "Noms/nom.html", {'form': foodform})

def detail(request,nom_id):
    food = get_object_or_404(Food_model, pk=nom_id)
    return render(request, "Noms/detail.html",{'food':food})
