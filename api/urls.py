from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.CreateListAPiView.as_view()),
    path('students/<int:pk>/', views.GetUpdateDelete.as_view())
    # path('students/',views.studentsView, name="create-student"),
    # path('students/<int:pk>/',views.studentupdate, name="update-student")
]