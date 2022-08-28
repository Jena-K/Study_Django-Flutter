from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo, Solution
from .serializers import TodoSerializer, SolutionSerializer


# Create your views here.

class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class SolutionView(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
