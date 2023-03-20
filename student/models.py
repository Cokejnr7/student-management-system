from django.db import models
from datetime import datetime as dt
from school.models import Faculty,Department,Programme
from django.core.validators import RegexValidator
# Create your models here.


GENDER = (
    ('M','male'),
    ('F','female')
)

TITLE = (
    ('MR','mister'),
    ('MRS','missus'),
    ('MISS', 'misses')
)


class Student(models.Model):
    matric_no = models.CharField(max_length=50,blank=True)
    passport_img = models.ImageField(upload_to = "passport/%Y/%m/%d")
    created_at = models.DateTimeField(auto_now_add=True)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    programme = models.ForeignKey(Programme,on_delete=models.PROTECT)
    #mode of entrance
    
    def save(self,*args, **kwargs):
        if not self.matric_no:
            year = dt.now().strftime('%y')
            faculty = "%02d" %self.faculty.id
            department = "%02d" %self.department.id
            total = Student.objects.filter(department=self.department,created_at = self.created_at).count()+1
            self.matric_no  = year + faculty + department + str(total)
                 
        super().save(self,*args, **kwargs)
        
    
    def __str__(self) -> str:
        return self.matric_no


class Biodata(models.Model):
    owner = models.OneToOneField(Student,on_delete=models.CASCADE)
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
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,validators=[RegexValidator(r'^\d{11,15}$')])
    next_of_kin = models.CharField(max_length=100)
    kin_phone_number = models.CharField(max_length=15,validators=[RegexValidator(r'^\d{11,15}$')])
    name_of_sponsor = models.CharField(max_length=100)
    sponsor_address = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'