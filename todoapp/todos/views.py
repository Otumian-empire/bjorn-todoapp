from rest_framework import viewsets, permissions

from .models import Todo
from .serializer import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by("id")
    serializer_class = TodoSerializer
    # permission_classes = [permissions.IsAuthenticated]
    