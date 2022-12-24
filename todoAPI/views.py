from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request 
from rest_framework import status
from rest_framework.views import APIView

from .models import Todo

from .serializers import TodoSerializer

# Create todo task

class CreateTodoView(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Get all todo tasks

class GetAllTodoView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Remove todo task by id
class RemoveTodoView(APIView):
    def get(self, request, id):
        # Check if todo task exists
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()        
            return Response(status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)