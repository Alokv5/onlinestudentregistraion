from  django import  forms
from app1.models import CourseModel

class CourseForm(forms.ModelForm):
  class Meta:
      model=CourseModel
      fields="__all__"
      labels={
          "name":"Student Name",
          "facutly":"Faculty Name",
          "date":"Date",
          "time":"Time",
          "fee":"FEE",
          "duration":"Duration"
      }