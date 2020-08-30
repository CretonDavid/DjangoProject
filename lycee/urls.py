from django.conf.urls import url
from . import views
from .views import StudentCreateView, StudentUpdateView, particular_Call, CursusCreateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cursus_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^liste_Call/$', views.liste_Call, name='liste_Call'),
    url(r'^student/(?P<student_id>[0-9]+)$', views.detail_student, name='detail_student'),
    url(r'^student/create/$', StudentCreateView.as_view(), name='create_student'),
    url(r'^cursus/create/$', CursusCreateView.as_view(), name='create_cursus'),
    url(r'^student/edit/(?P<pk>[0-9]+)$', StudentUpdateView.as_view(), name='edit_student'),
    url(r'^cursusCall/(?P<cursus_id>[0-9]+)$', views.cursusCall, name='call_of_roll'),
    url(r'^particular_Call/$', particular_Call.as_view(), name='particular_call'),
    url(r'^detail_Call/(?P<appel_list_id>[0-9]+)$', views.detail_Call, name='detail_Call'),
    url(r'^detail_particular_Call/$', views.detail_particular_Call, name='detail_particular_Call')]
