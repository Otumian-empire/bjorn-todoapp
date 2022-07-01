from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from rest_framework import viewsets, permissions
from rest_framework.parsers import JSONParser

from .serializer import ClientSerializer

@csrf_exempt
@require_POST
def create_client_view(request):
    
    response = {
        "success": False, 
        "message":"Registration unsuccessful"
    }

    try:
        request_body = JSONParser().parse(request)
        entity = ClientSerializer(data=request_body)

        if entity.is_valid(raise_exception=True):
            entity.save()

            response["success"] = True
            response["message"] = "Registration successful"
        else:
            response.update(**entity.errors)
        
    except Exception as e:
        print(e)
        response["message"] = "Invalid credentials"
    
    return JsonResponse(
        safe=True, 
        data=response
    )
