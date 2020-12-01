from rest_framework.viewsets import ModelViewSet
from core.models import Student, Group, MyUser
from api.serializers import StudentSerializer, GroupSerializer, TeacherSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TeacherViewSet(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = TeacherSerializer
