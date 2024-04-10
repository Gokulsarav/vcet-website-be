
import json
from django.http import JsonResponse
from .models import LabData

def store_lab_data(request):
    return get_lab_data(request)

def get_lab_data(request):
    # Retrieve all LabData objects from the database
    lab_data = LabData.objects.all().values()

    # Convert queryset to list of dictionaries
    lab_data_list = list(lab_data)

    # Return JSON response with the fetched data
    return JsonResponse({'LabData': lab_data_list})
