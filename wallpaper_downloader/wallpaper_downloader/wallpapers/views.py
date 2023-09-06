from django.shortcuts import render
from django.views import View
from .tasks import download_random_wallpaper


def home(request):
    if request.method == 'POST':
        orientation_type = request.POST.get('orientation_type')
        download_random_wallpaper.delay(orientation_type)
    return render(request, 'wallpapers/template.html')
