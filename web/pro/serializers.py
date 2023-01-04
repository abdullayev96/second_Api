from  rest_framework.serializers import ModelSerializer
from .models import Task, Company

class TaskSerializer(ModelSerializer):
    class Meta:
        model= Task
        fields = ("title", "completed", "number", "create_at")


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ("name", "country", "address", "number", "images", "create_at")


