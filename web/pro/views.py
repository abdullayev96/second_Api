# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import  TaskSerializer
# from .models import Task
#
#
#
# @api_view(['GET', 'POST'])
# def task_list(request):
#     if request.method == 'GET':
#         tasks=Task.objects.all()
#         serializer=TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer=TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'POST', 'DELETE'])
# def task_details(request, pk):
#     try:
#         tasks=Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_400_Not_FOUND, data=request.data)
#
#     if request.method == 'GET':
#         serializer=TaskSerializer(tasks)
#         return Response(serializer.data)


from .models import Task, Company
from .serializers import TaskSerializer, CompanySerializer
from rest_framework.generics import ListCreateAPIView


class TaskApiView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CompanyApiView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer









