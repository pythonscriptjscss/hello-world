from django.shortcuts import render
from student.models import profile
def all_data(req):
    stu = profile.objects.all()
    return render(req,'student/all.html')
