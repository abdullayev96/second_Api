from django.urls import path
from .views import TaskApiView, CompanyApiView


urlpatterns=[
    path("task/",TaskApiView.as_view(), name='task_list'),
    path("com/", CompanyApiView.as_view(), name="company_list")
]