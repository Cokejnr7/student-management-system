from rest_framework import viewsets
from .models import Department,Faculty,Programme,Course
from .serializer import DepartmentSerializer,FacultySerialzer,ProgrammeSerializer,CourseSerializer
# from .permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated,IsAdminUser


# Create your views here.
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminUser,IsAuthenticated]
    

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerialzer
    permission_classes = [IsAdminUser,IsAuthenticated]
    

class ProgrammeViewSet(viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
    permission_classes = [IsAdminUser,IsAuthenticated]
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser,IsAuthenticated]