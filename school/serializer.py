from rest_framework import serializers
from .models import Department,Faculty,Programme,Course


class FacultySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
        
        
class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = '__all__'
        

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields  = '__all__'