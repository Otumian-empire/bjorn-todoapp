from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from rest_framework import viewsets, permissions
from rest_framework.parsers import JSONParser

from .serializer import ClientSerializer

@csrf_exempt
@require_POST
def create_client_view(request):
    
    try:
        request_body = JSONParser().parse(request)
        entity = ClientSerializer(data=request_body)

        if entity.is_valid():
            entity.save()
           
            return JsonResponse(
                safe=True, 
                data= {
                    "success": True, 
                    "message":"Registration successful"
                }
            )
        
        return JsonResponse(
            safe=True, 
            data= {
                "success": False, 
                "message":"Registration Unsuccessful - invalid",
                **entity.errors,
            },
        )
    except Exception as e:
        print(e)
        return JsonResponse(
            safe=True, 
            data= {
                "success": False, 
                "message":"Registration unsuccessful - error"
            }
        )
