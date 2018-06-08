from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Brokers

def brokers_list(request):
    brokers = Brokers.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'brokers/brokers_list.html', {'broker': brokers})


def broker_detail(request, pk):
    broker = get_object_or_404(Brokers, pk=pk)
    return render(request, 'brokers/broker_detail.html', {'broker': brokers})

