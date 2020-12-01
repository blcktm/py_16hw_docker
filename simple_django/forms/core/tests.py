from django.urls.base import reverse_lazy
from django.test import TestCase, Client
from core.models import Group, MyUser, Student


class DiagnosticTestCase(TestCase):

    def setUp(self):

        self.client = Client()

        self.user = MyUser(
            username='testadmin', email='test@example.com', is_active=True,
            is_staff=True, is_superuser=True,
        )
        self.user.set_password('test')
        self.user.save()

        self.client.login(username='testadmin', password='test')

        teacher = MyUser.objects.create(username='test')
        students_lst = []
        groups_lst = []

        for counter in range(10):
            students_lst.append(Student(
                id=counter
            ))
            groups_lst.append(Group(
                id=counter,
                teacher=teacher
            ))
        Student.objects.bulk_create(students_lst)

        for group in groups_lst:
            group.students.set(students_lst)
        Group.objects.bulk_create(groups_lst)

    def test_groupsandstudents_page(self):
        response = self.client.get(reverse_lazy('core:groupsandstudents', kwargs={'username': 'test'}))
        self.assertIn('user', response.context)
        self.assertEqual(response.status_code, 200)

    def test_groupsandstudents_groups_count(self):
        response = self.client.get(reverse_lazy('core:groupsandstudents', kwargs={'username': 'test'}))
        self.assertEqual(len(response.context['groups']), 10)

    def test_groupsandstudents_students_count(self):
        response = self.client.get(reverse_lazy('core:groupsandstudents', kwargs={'username': 'test'}))
        groups = response.context['groups']

        for group in groups:
            self.assertEqual(group.students.count(), 10)

    def test_home_page(self):
        response = self.client.get(reverse_lazy('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_teachers_page(self):
        response = self.client.get(reverse_lazy('core:teachers'))
        self.assertEqual(response.status_code, 200)

    def test_allteachers_page(self):
        response = self.client.get(reverse_lazy('core:allteachers'))
        self.assertEqual(response.status_code, 200)

    def test_students_page(self):
        response = self.client.get(reverse_lazy('core:students'))
        self.assertEqual(response.status_code, 200)

    def test_create_teacher_page(self):
        response = self.client.get(reverse_lazy('core:create-teacher'))
        self.assertEqual(response.status_code, 200)

    def test_create_student_page(self):
        response = self.client.get(reverse_lazy('core:create-student'))
        self.assertEqual(response.status_code, 200)

    def test_create_group_page(self):
        response = self.client.get(reverse_lazy('core:create-group'))
        self.assertEqual(response.status_code, 200)

    def test_update_teacher_page(self):
        response = self.client.get(reverse_lazy('core:update-teacher', kwargs={'username': 'testadmin'}))
        self.assertEqual(response.status_code, 200)

    def test_update_group_page(self):
        group = Group.objects.first()
        response = self.client.get(reverse_lazy('core:update-group', kwargs={'group_id': group.id}))
        self.assertEqual(response.status_code, 200)

    def test_update_student_page(self):
        student = Student.objects.first()
        response = self.client.get(reverse_lazy('core:update-student', kwargs={'student_id': student.id}))
        self.assertEqual(response.status_code, 200)

    def test_delete_student_page(self):
        student = Student.objects.first()
        response = self.client.get(reverse_lazy('core:delete-student', kwargs={'student_id': student.id}))
        self.assertEqual(response.status_code, 200)

    def test_delete_group_page(self):
        group = Group.objects.first()
        response = self.client.get(reverse_lazy('core:delete-group', kwargs={'group_id': group.id}))
        self.assertEqual(response.status_code, 200)

    def test_delete_teacher_page(self):
        response = self.client.get(reverse_lazy('core:delete-teacher', kwargs={'username': 'testadmin'}))
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get(reverse_lazy('core:contact'))
        self.assertEqual(response.status_code, 200)

    def test_success_page(self):
        response = self.client.get(reverse_lazy('core:success'))
        self.assertEqual(response.status_code, 200)

    def test_registration_page(self):
        response = self.client.get(reverse_lazy('core:registration'))
        self.assertEqual(response.status_code, 200)

    def test_admin_page(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
