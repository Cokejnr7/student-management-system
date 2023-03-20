from django.db import models
from registration.models import Registration
from .validators import validate_gpa

# Create your models here.

class Result:
    # semester = 
    # session
    registration = models.OneToOneField(Registration,on_delete=models.CASCADE)
    gpa = models.DecimalField(max_digits=3,decimal_places=2,validators=[validate_gpa],blank=True)
    cgpa = models.DecimalField(max_digits=3,decimal_places=2,validators=[validate_gpa],blank=True)
    
    
    # def save(self,*args, **kwargs):
    #     if not self.gpa:
    #         self.registration.courseregistration:
    
    
# class Grade:
    