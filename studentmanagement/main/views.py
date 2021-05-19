
from django.http import HttpResponse

from django.shortcuts import render
from django.views import View
from django.views.generic import (
   DetailView,
   ListView,
   UpdateView,
   DeleteView,
   CreateView
 )
# Create your views here.
from main import models

class  Index(View):
    def get(self, request):
        return HttpResponse("GEt request")
    def post(self, request):
        return HttpResponse("POST request")

class CollegeDetail(DetailView):
    model = models.College
    template_name = 'college_detail.html'

# 5 generic views 1. Detail_view 2. list view 3. Create view 4. Update view 5.DELETE VIEW

class CollegeList(ListView):
    model = models.College
    template_name = 'college_list.html'
    context_object_name = 'colleges'

class CollegeCreate(CreateView):
    model = models.College
    template_name = 'college_create.html'
    fields = '__all__'
    success_url = '/college'
class CollegeUpdate(UpdateView):
    model = models.College
    template_name = 'college_create.html'
    fields = '__all__'
    success_url = '/college'


class StudentCreate(CreateView):
    model = models.Student
    template_name = 'student_create.html'
    fields = '__all__'
    success_url = '/'

class StudentDelete(DeleteView):
    model = models.Student
    template_name = 'confirm.html'
    fields = '__all__'
    success_url = '/'