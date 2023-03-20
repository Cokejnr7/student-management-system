from rest_framework import generics,status
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Student,Biodata

# Create your views here.

class StudentCreateView(generics.GenericAPIView):
    serializer_class = StudentSerializer
    
    def post(self,request):
        
        #expecting dictionary with student and biodata key
        data = request.data
        
        if data.get("student") is None:
            return Response({"detail":"No Order Items"},status=status.HTTP_400_BAD_REQUEST)
        
        if data.get("biodata") is None:
            return Response({"detail":"No Order Items"},status=status.HTTP_400_BAD_REQUEST)
        
        # try:
            # student = Student()
        # biodata = Biodata()
        # pass