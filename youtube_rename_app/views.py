from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import *
# Create your views here.


def dashboard(request):
    return render(request, 'youtube_rename_app/dashboard.html',{})


def name_updater_poll(request, pk):
    update_request = Name_Update_Request.objects.filter(pk=pk).first()
    return JsonResponse({'status': update_request.status})

def name_updater(request):
    update_request = Name_Update_Request()
    update_request.start_date_time = timezone.now()
    update_request.save()
    update_request.start_update()
    
    return JsonResponse({'pk': update_request.pk})