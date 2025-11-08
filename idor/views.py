from django.shortcuts import render
from .models import Student
from django.http import JsonResponse
def list_all_students(request):
    students = Student.objects.all()
    context = {'students' : students}
    
    return render(request, 'idor/students.html', context=context)


def student_info(request, pk):
    student = Student.objects.get(id=pk)
    context = {'student' : student}
    return render(request, "idor/student_info.html", context=context)


def json_data(request, pk):
    student = Student.objects.get(id=pk)
    data = {'first_name' : student.first_name,
            'last_name' : student.last_name,
            'average_mark' : student.avg_mark}
    return JsonResponse(data)