from django.db import models
from datetime import datetime as dt
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Student(models.Model):
    pass
    # matric_no = models.CharField()
    # passport_img = models.ImageField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # faculty = models.ForeignKey(Faculty,on_delete=models.SET_NULL)
    # department = models.ForeignKey(Department,on_delete=models.SET_NULL)
    # programme = models.ForeignKey(Programme,on_delete=models.SET_NULL)
    #mode of entrance
    
    # def save(self,*args, **kwargs):
    #     if not self.matric_no:
    #         year = self.created_at.strftime('%y')
    #         faculty = "%02d" %self.faculty.id
    #         department = "%02d" %self.department.id
    #         self.matric_no  = year + faculty + department + 
            
            
        # super().save(self,*args, **kwargs)



GENDER = (
    ('M','male'),
    ('F','female')
)

TITLE = (
    ('MR','mister'),
    ('MRS','missus'),
    ('MISS', 'misses')
)

class Biodata(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    title = models.CharField(max_length=200,choices=TITLE)
    gender = models.CharField(max_length=50,choices=GENDER)
    nationality = models.CharField(max_length=100)
    state_of_origin = models.CharField(max_length=100)
    local_government = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    religion = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True)
    next_of_kin = models.CharField(max_length=100)
    kin_phone_number = PhoneNumberField(blank=True)
    name_of_sponsor = models.CharField(max_length=100)
    sponsor_address = models.CharField(max_length=200)