from django.db import models
from safedelete.models import SafeDeleteMixin, SOFT_DELETE_CASCADE  

class Student(SafeDeleteMixin):
    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.AutoField(primary_key=True)
    student_name = models.TextField()
    student_age = models.TextField()
    student_cccd = models.TextField()
    student_email = models.TextField()
    student_sex = models.TextField()
    student_class = models.TextField()
    student_address = models.TextField()
    student_img = models.TextField()
    
    class Meta:
        db_table = "student"