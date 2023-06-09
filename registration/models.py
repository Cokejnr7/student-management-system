from django.db import models
from student.models import Student
from school.models import Course

# Create your models here.

SEMESTER = (
    ('first','First'),
    ('second','Second'),
    )


class Registration(models.Model):
    semester = models.CharField(max_length=20,choices=SEMESTER)
    # session = models.CharField()
    # student =  models.ForeignKey(Student,on_delete=models.CASCADE,related_name="registrations")
    
    
class CourseRegistration(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="registration")
    registration = models.ForeignKey(Registration,on_delete=models.CASCADE,related_name="courses")
    # grade = models.OneToOneField()
    
    class Meta:
        unique_together = ['course','registration']