from django.db import models
from .validators import valid_level,valid_unit
from django.core.exceptions import ValidationError
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
    abbv = models.CharField(max_length=3,null=True)
    
    def __str__(self) -> str:
        return self.name



class Programme(models.Model):
    years = models.IntegerField()
    programme_type = models.CharField(max_length=30,choices=PROGRAMME)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="programmes")
    degree = models.CharField(max_length=150)
    
    def clean(self):
        if self.programme_type == "undergraduate" and self.years < 4:
            raise ValidationError(f"minimum of 4 years for {self.programme_type} programmes")
        
        elif self.programme_type == "postgraduate" and self.years<1:
            raise ValidationError(f"minimum of 1 year for {self.programme_type} programmes")
        
    def save(self,*args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.programme_type} ({self.degree})'
    


class Course(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="courses")
    programme = models.ForeignKey(Programme,on_delete=models.CASCADE,related_name="courses")
    code = models.CharField(max_length=3)
    semester = models.CharField(max_length=15,choices=SEMESTER, default=SEMESTER[0][0])
    level = models.IntegerField(validators=[valid_level])
    unit = models.IntegerField(validators=[valid_unit])
    description = models.TextField()
    is_compulsory = models.BooleanField(default=True)
    instructor = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        if self.department.abbv:
            return f'{self.department.abbv} {self.code}'
        return self.code
    
       
class Session(models.Model):
    start_year = models.DateField()
    end_year = models.DateField()
    