from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader
from django.views import View

from .models import (
    Instructor,
    Section,
    Course,
    Semester,
    Student,
    Registration,


)


# def instructor_list_view(request):
#     instructor_list = Instructor.objects.all()
#     # instructor_list = Instructor.objects.none()
#     template = loader.get_template(
#         'courseinfo/instructor_list.html')
#     context = {'instructor_list': instructor_list}
#     output = template.render(context)
#     return HttpResponse(output)


class InstructorList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/instructor_list.html',
            {'instructor_list': Instructor.objects.all()}
        )


class SectionList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/section_list.html',
            {'section_list': Section.objects.all()}
        )


class CourseList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/course_list.html',
            {'course_list': Course.objects.all()}
        )


class SemesterList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/semester_list.html',
            {'semester_list': Semester.objects.all()}
        )


class StudentList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/student_list.html',
            {'student_list': Student.objects.all()}
        )


class RegistrationList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/registration_list.html',
            {'registration_list': Registration.objects.all()}
        )