from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only tasks belonging to the authenticated user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the logged-in user to the task
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.is_completed = True
        task.save()
        return Response(
            {"message": "Task marked as completed"},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'])
    def incomplete(self, request, pk=None):
        task = self.get_object()
        task.is_completed = False
        task.save()
        return Response(
            {"message": "Task marked as incomplete"},
            status=status.HTTP_200_OK
        )
