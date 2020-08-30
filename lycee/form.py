from django.forms.models import ModelForm
from .models import Student, Presence, Cursus


class StudentForm(ModelForm):

  class Meta:
    # la ref du ModEle
    model = Student

    # liste des champs A Editer
    fields  = (
      "first_name",
      "last_name",
      "birth_date",
      "email",
      "phone",
      "comments",
      "cursus",
    )

class CursusForm(ModelForm):

  class Meta:
    # la ref du ModEle
    model = Cursus

    # liste des champs A Editer
    fields  = (
      "name",
      "year_from_bac",
      "scholar_year",
    )

class Particular(ModelForm):

  class Meta:
    # la ref du ModEle
    model = Presence

    # liste des champs A Editer
    fields = (
      "date",
      "isAbsent",
      "reason",
      "student",
      )