from django.http import HttpResponse
from django.shortcuts import redirect, render
from listings.models import Band
from listings.templates.listings.forms import BandForm

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html',{'bands':bands})
   # return render(request, 'listings/hello.html')

def band_detail(request,band_id):
    band = Band.objects.get(id = band_id)
    return render(request, 'listings/band_detail.html', {'band':band})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

# les formulaires
def BandCreate(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band_detail',band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form':form})

def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band_detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request,
        'listings/band_update.html',
        {'form': form})

