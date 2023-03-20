from rest_framework import serializers
from .models import Student,Biodata


class BiodataSerializer():
        class Meta:
            model = Biodata
            fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    matric_no = serializers.ReadOnlyField()
    biodata = BiodataSerializer()
    class Meta:
        model = Student
        fields = '__all__'


            
            