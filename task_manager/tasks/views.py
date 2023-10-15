from rest_framework import viewsets
from .serializers import task_serializer
from .models import task

class task_viewset(viewsets.ModelViewSet):
    queryset=task.objects.all()
    serializer_class=task_serializer