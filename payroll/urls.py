from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.ReportsList.as_view(), name="reports"),
    path('upload/', views.FileUploadView.as_view())
]