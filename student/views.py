from rest_framework import generics,status
from rest_framework.response import Response
from .serializer import StudentSerializer
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser
from .models import Student,Biodata
import json

# Create your views here.

class StudentCreateView(generics.GenericAPIView):
    serializer_class = StudentSerializer
    parser_classes = [FormParser,MultiPartParser,JSONParser]
    
    def post(self,request):
        
        #expecting dictionary with student and biodata key
        data = dict(request.data)
        
        if data.get("student") is None:
            return Response({"detail":"Student not provided."},status=status.HTTP_400_BAD_REQUEST)
        
        if data.get("biodata") is None:
            return Response({"detail":"Biodata not provided."},status=status.HTTP_400_BAD_REQUEST)
        
        
        student_data = json.loads(data.get("student")[0])
        biodata = json.loads(data.get("biodata")[0])
        print(student_data)
        
        return Response("hello",status=status.HTTP_201_CREATED)
        
        # try:
            # student = Student()
        # biodata = Biodata()
        # pass