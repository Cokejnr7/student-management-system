from rest_framework import serializers
from .models import Student,Biodata


class BiodataSerializer():
        class Meta:
            model = Biodata
            fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    biodata = BiodataSerializer()
    class Meta:
        model = Student
        fields = '__all__'


            
            