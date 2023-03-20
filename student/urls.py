from django.urls import path
from .views import StudentCreateView

urlpatterns = [
    path('students/',StudentCreateView.as_view()),
]
