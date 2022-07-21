from django.http import JsonResponse
from .models import sijan
from .serializers import sijanSerializer

def sijanList(request): 
    dataall= sijan.objects.all()
    serializer = sijanSerializer(dataall, many=True)
    return JsonResponse({'sijan':serializer.data})