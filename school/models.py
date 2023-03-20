from django.db import models

# Create your models here.

SEMESTER = (
    ('first','First'),
    ('second','Second'),
    )


PROGRAMME = (
    ('undergraduate','Undergraduate'),
    ('postgraduate','Postgraduate')
             )


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE,related_name="departments")
    
    def __str__(self) -> str:
        return self.name



class Programme(models.Model):
    years = models.IntegerField()
    programme_type = models.CharField(max_length=30,choices=PROGRAMME)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="programmes")
    degree = models.CharField(max_length=150)
    # degree = MSC |PHD|MPhil|PGDip
    
    def __str__(self) -> str:
        return self.programme_type
    


class Course(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="courses")
    code = models.CharField(max_length=20)
    semester = models.CharField(max_length=15,choices=SEMESTER, default=SEMESTER[0][0])
    level = models.IntegerField()
    unit = models.IntegerField()
    description = models.TextField()
    is_compulsory = models.BooleanField(default=True)
    instructor = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
       
class Session(models.Model):
    start_year = models.DateField()
    end_year = models.DateField()
    