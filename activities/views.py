from django.shortcuts import render
from django.utils import timezone
from .models import BenchmarkingEntry, MediaMention, Event


def index(request):
    return render(request, 'activities/index.html')


def benchmarking(request):
    entries = BenchmarkingEntry.objects.all()
    return render(request, 'activities/benchmarking.html', {'entries': entries})


def media(request):
    mentions = MediaMention.objects.all()
    return render(request, 'activities/media.html', {'mentions': mentions})


def events(request):
    today = timezone.now().date()
    upcoming = Event.objects.filter(date__gte=today).order_by('date')
    past = Event.objects.filter(date__lt=today).order_by('-date')
    return render(request, 'activities/events.html', {'upcoming': upcoming, 'past': past})