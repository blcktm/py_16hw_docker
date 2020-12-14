from django.urls import path
from core.views import IndexView, GroupsAndStudentsView, RegistrationView, contactView, successView, TeacherCreateView, \
    StudentCreateView, GroupCreateView, TeacherUpdateView, GroupUpdateView, StudentUpdateView, GroupDeleteView, \
    StudentDeleteView, TeacherDeleteView, AllTeachersView, TeachersView, StudentsView, ExportStudentList, JsView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('teachers/', TeachersView.as_view(), name='teachers'),
    path('allteachers/', AllTeachersView.as_view(), name='allteachers'),
    path('students/', StudentsView.as_view(), name='students'),
    path('create-teacher/', TeacherCreateView.as_view(), name='create-teacher'),
    path('create-student/', StudentCreateView.as_view(), name='create-student'),
    path('create-group/', GroupCreateView.as_view(), name='create-group'),
    path('update-teacher/<str:username>/', TeacherUpdateView.as_view(), name='update-teacher'),
    path('update-group/<int:group_id>/', GroupUpdateView.as_view(), name='update-group'),
    path('update-student/<int:student_id>/', StudentUpdateView.as_view(), name='update-student'),
    path('delete-student/<int:student_id>/', StudentDeleteView.as_view(), name='delete-student'),
    path('delete-group/<int:group_id>/', GroupDeleteView.as_view(), name='delete-group'),
    path('delete-teacher/<str:username>/', TeacherDeleteView.as_view(), name='delete-teacher'),
    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('groupsandstudents/<str:username>/', GroupsAndStudentsView.as_view(), name='groupsandstudents'),
    path('export', ExportStudentList.as_view(), name='export'),
    path('js-crud/', JsView.as_view(), name='js-crud'),
]
