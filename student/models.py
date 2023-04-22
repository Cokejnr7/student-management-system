from django.db import models
from datetime import datetime as dt
from school.models import Faculty,Department,Programme
from django.core.validators import RegexValidator
from .validators import is_image,check_size
# Create your models here.


GENDER = (
    ('M','male'),
    ('F','female')
)

TITLE = (
    ('MR','mr'),
    ('MRS','mrs'),
    ('MISS', 'miss')
)


class Student(models.Model):
    matric_no = models.CharField(max_length=50,blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    passport_img = models.ImageField(upload_to = "passport/%Y/%m/%d",validators=[is_image,check_size])
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
                 
        super(Student,self).save(*args,**kwargs)
        
    
    def __str__(self) -> str:
        return self.matric_no


class Biodata(models.Model):
    owner = models.OneToOneField(Student,on_delete=models.CASCADE,related_name="biodata")
    first_name = models.CharField(max_length=150,blank=True)
    last_name = models.CharField(max_length=150,blank=True)
    middle_name = models.CharField(max_length=150)
    title = models.CharField(max_length=200,choices=TITLE)
    gender = models.CharField(max_length=50,choices=GENDER)
    nationality = models.CharField(max_length=100)
    state_of_origin = models.CharField(max_length=100)
    local_government = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    religion = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15,validators=[RegexValidator(r'^\d{11,15}$')])
    next_of_kin = models.CharField(max_length=100)
    kin_phone_number = models.CharField(max_length=15,validators=[RegexValidator(r'^\d{11,15}$')])
    name_of_sponsor = models.CharField(max_length=100)
    sponsor_address = models.CharField(max_length=200)
    
    def save(self,*args, **kwargs):
        if self.owner:
            self.first_name = self.owner.first_name
            self.last_name = self.owner.last_name
            self.email = self.owner.email
        
        super(Biodata,self).save(*args,**kwargs)
        
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    