from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Student


User = get_user_model()

@receiver(post_save,sender=Student)
def create_student_user(sender,instance,created,**kwargs):
    student = instance
    if created:
        user = User()
        user.username = student.matric_no
        user.email = student.email
        user.set_password(student.last_name)
        
        user.save()