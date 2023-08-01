from django import forms
from .models import Student
import re
class StdForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "student_name",
            "student_age",
            "student_cccd",
            "student_email",
            "student_sex",
            "student_class",
            "student_address",
            "student_img",
        ]
    def clean_username(self):
        student_name = self.cleaned_data['student_name']
        if not re.search(r'^\w+$', student_name):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            Student.objects.get(student_name=student_name)
        except Student.DoesNotExist:
            return student_name
        raise forms.ValidationError("Tài khoản đã tồn tại")