from django.contrib import admin
from .models import Faculty,Department,Course,Session,Programme
# Register your models here.


admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(Programme)