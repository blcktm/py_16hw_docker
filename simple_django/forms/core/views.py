import csv
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import FormView, View, ListView
from django.contrib.auth.models import User
from django.db.models import Avg, Max, Min, Count
from django.urls.base import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError
from core.forms import GroupForm, StudentForm, ContactUS, RegistrationForm
from core.models import Student, Group, get_user_model
from core.tasks import send_mail_celery
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


# class JsView(TemplateView):
#     template_name = 'js_template.html'
@method_decorator(cache_page(10 * 60), 'get')
class JsView(ListView):
    template_name = 'js_template.html'
    model = Student
    context_object_name = 'students'

    def get_context_data(self, *args, **kwargs):
        self.request.session['refresh_count_index'] = self.request.session.get('refresh_count_index', 0) + 1
        context = super(JsView, self).get_context_data(*args, **kwargs)
        context['form'] = StudentForm
        context['refresh_count_index'] = self.request.session['refresh_count_index']
        return context


class UpdateFormAjax(UpdateView):
    template_name = 'update_student.html'
    model = Student
    # success_url = '/'
    form_class = StudentForm
    context_object_name = 'student'


class CreateFormAjax(CreateView):
    template_name = 'create.html'
    model = Student
    form_class = StudentForm
    # context_object_name = 'student'


@method_decorator(cache_page(1 * 60), 'get')
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        self.request.session['refresh_count_index'] = self.request.session.get('refresh_count_index', 0) + 1

        context = super(IndexView, self).get_context_data(*args, **kwargs)

        groups = Group.objects.all().values('id', 'name', 'teacher').annotate(
            student_count=Count('students'),
            student_avg=Avg('students__age'),
            student_max=Max('students__age'),
            student_min=Min('students__age'),
        )

        teachers = get_user_model().objects.all()

        context = {
            'settings': settings,
            'teachers': teachers,
            'groups': groups,
            'count_words': self.request.GET.get('count_words', '0'),
            'refresh_count_index': self.request.session['refresh_count_index']
        }

        return context


@method_decorator(cache_page(2 * 60), 'get')
class StudentsView(TemplateView):
    template_name = "students.html"

    def get_context_data(self, **kwargs):
        self.request.session['refresh_count_students'] = self.request.session.get('refresh_count_students', 0) + 1
        students = Student.objects.all()
        return {
            'students': students,
            'refresh_count_students': self.request.session['refresh_count_students']
        }


@method_decorator(cache_page(3 * 60), 'get')
class TeachersView(TemplateView):
    template_name = "teachers.html"

    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        self.request.session['refresh_count_teachers'] = self.request.session.get('refresh_count_teachers', 0) + 1
        groups = Group.objects.all().values('id', 'name', 'teacher')

        return {
            'groups': groups,
            'refresh_count_teachers': self.request.session['refresh_count_teachers']
        }


class ExportStudentList(View):

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="students.csv"'
        writer = csv.writer(response)
        writer.writerow(['first_name', 'last_name', 'age', 'phone'])

        for student in Student.objects.all():
            writer.writerow([student.first_name, student.last_name, student.age, student.phone])
        return response


class GroupsAndStudentsView(TemplateView):
    template_name = "groupsandstudents.html"

    def get_context_data(self, **kwargs):
        groups = Group.objects.filter(teacher__username=kwargs['username']).prefetch_related('students')
        return {
            'groups': groups,
        }


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('main:home')


def contactView(request):
    if request.method == 'GET':
        form = ContactUS()
    else:
        form = ContactUS(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            try:
                send_mail_celery.delay(title, sender, message)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('main:success')
    return render(request, "contact.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')


class AllTeachersView(TemplateView):
    template_name = "allteachers.html"

    def get_context_data(self, **kwargs):
        allteachers = get_user_model().objects.all()
        return {
            'allteachers': allteachers
        }


class TeacherCreateView(CreateView):
    template_name = 'create.html'

    success_url = reverse_lazy('main:teachers')
    model = get_user_model()
    fields = '__all__'


class StudentCreateView(CreateView):
    template_name = 'create.html'

    success_url = reverse_lazy('main:teachers')
    model = Student
    fields = '__all__'


class GroupCreateView(FormView):
    template_name = 'create.html'

    form_class = GroupForm
    success_url = reverse_lazy('main:teachers')

    def form_valid(self, form):
        form.save()
        return super(GroupCreateView, self).form_valid(form)


class TeacherUpdateView(UpdateView):
    template_name = 'update_teacher.html'

    success_url = reverse_lazy('main:allteachers')
    model = get_user_model()
    form_class = RegistrationForm
    slug_field = "username"
    slug_url_kwarg = "username"


class StudentUpdateView(UpdateView):
    template_name = 'update_student.html'

    success_url = reverse_lazy('main:js-crud')  # reverse_lazy('main:students')
    model = Student
    form_class = StudentForm
    pk_url_kwarg = 'student_id'


class GroupUpdateView(UpdateView):
    template_name = 'update_group.html'

    success_url = reverse_lazy('main:teachers')
    model = Group
    form_class = GroupForm
    pk_url_kwarg = 'group_id'


class TeacherDeleteView(DeleteView):
    template_name = 'delete.html'

    model = get_user_model()
    success_url = reverse_lazy('main:allteachers')
    slug_field = "username"
    slug_url_kwarg = "username"


class GroupDeleteView(DeleteView):
    template_name = 'delete.html'

    model = Group
    pk_url_kwarg = 'group_id'
    success_url = reverse_lazy('main:teachers')


class StudentDeleteView(DeleteView):
    template_name = 'delete.html'

    model = Student
    pk_url_kwarg = 'student_id'
    success_url = reverse_lazy('main:students')
