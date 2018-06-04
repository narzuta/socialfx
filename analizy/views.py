from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Analiza

def analiza_list(request):
    analizy = Analiza.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'analizy/analiza_list.html', {'analizy': analizy})


def analiza_detail(request, pk):
    analiza = get_object_or_404(Analiza, pk=pk)
    return render(request, 'analizy/analiza_detail.html', {'analiza': analiza})

