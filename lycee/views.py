from datetime import datetime

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Cursus, Student, Presence, Appel_list
from .form import StudentForm, Particular, CursusForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse
from django.shortcuts import get_object_or_404


#def index(request):
#  return HttpResponse("Racine de lycee")

# index : utilisation de HttpResponse
#def index(request):
#  result_list = Cursus.objects.order_by('name')
#  # chargement du template
#  template = loader.get_template('lycee/index.html')
#  # contexte
#  context = { 'liste' : result_list}
#  return HttpResponse(template.render(context, request))

# index : variante avec template intEgrE
def index (request):
  result_list = Cursus.objects.order_by('name')
  # contexte
  context = { 'liste' : result_list}
  # utilisation du template intEgrE
  return render (request, 'lycee/index.html', context)

def detail(request, cursus_id):
  result_list = Student.objects.filter(cursus_id = cursus_id)
  template = loader.get_template('lycee/student/detail_cursus.html')
  context = { 'liste' : result_list}
  return HttpResponse(template.render(context, request))

def detail_student(request,student_id):
    #result_list = Student.objects.get(pk=student_id)
    result_list = get_object_or_404(Student, pk=student_id)
    # context
    context = {'liste': result_list}
    return render (request, 'lycee/student/detail_student.html' , context)

def liste_Call(request):
  result_list = Appel_list.objects.order_by("date")
  template = loader.get_template('lycee/CallOfRoll/liste_Call.html')
  context = { 'liste' : result_list}
  return HttpResponse(template.render(context, request))

def detail_Call(request,appel_list_id):
    result_list = Presence.objects.filter(appel_list_id=appel_list_id)
    template = loader.get_template('lycee/CallOfRoll/detail_Call.html')
    context = {'liste': result_list,'cursus':result_list[0].cursus,'date':result_list[0].date}
    return HttpResponse(template.render(context, request))

def detail_particular_Call(request):
    result_list = Presence.objects.filter(cursus__isnull=True)
    template = loader.get_template('lycee/CallOfRoll/detail_particular_Call.html')
    context = {'liste': result_list}
    return HttpResponse(template.render(context, request))

def cursusCall(request, cursus_id):

    if request.method == 'POST':
        student_list = Student.objects.filter(cursus_id=cursus_id)
        cursus = Cursus.objects.get(id=cursus_id)
        appel_list = Appel_list(date=request.POST.get('date'),cursus=cursus)
        appel_list.save()
        for student in student_list:
            data = request.POST.get(str(student.id))
            if data == 'on':
                #student is absent
                callofroll = Presence(isAbsent=True, date=request.POST.get('date'), student=student, cursus=cursus, appel_list=appel_list)
            else:
                # student is present
                callofroll = Presence(isAbsent=False, date=request.POST.get('date'), student=student, cursus=cursus, appel_list=appel_list)
            callofroll.save()
        result_list = Cursus.objects.order_by('name')
        context = {'liste': result_list}
        return render(request, 'lycee/index.html', context)
    else:
        student_list = Student.objects.filter(cursus_id = cursus_id)
        cursus = Cursus.objects.get(id = cursus_id)
        context = {'liste': student_list, 'cursus': cursus}
        return render(request, 'lycee/CallOfRoll/cursusCall.html', context)

class StudentCreateView(CreateView):
  # ref au modEle
  model = Student
  # ref au formulaire
  form_class = StudentForm
  # le nom du render
  template_name = "lycee/student/create.html"

  # page appelEe si creation ok
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

class StudentUpdateView(UpdateView):
   # ref au modEle
   model = Student
   # ref au formulaire
   form_class = StudentForm
   # le nom du render
   template_name = "lycee/student/create.html"

   # page appelEe si creation ok
   def get_success_url(self):
       return reverse("detail_student", args=(self.object.pk,))

class CursusCreateView(CreateView):
  # ref au modEle
  model = Cursus
  # ref au formulaire
  form_class = CursusForm
  # le nom du render
  template_name = "lycee/cursus/create.html"

  # page appelEe si creation ok
  def get_success_url(self):
    return reverse ("detail_cursus", args=(self.object.pk,))

class particular_Call(CreateView):
    # ref au modEle
    model = Presence
    # ref au formulaire
    form_class = Particular
    # le nom du render
    template_name = "lycee/CallOfRoll/particular_Call.html"

    def get_success_url(self):
        return reverse("index")