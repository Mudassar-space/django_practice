from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.studentsView, name="create-student"),
    path('students/<int:pk>/',views.studentupdate, name="update-student")
]