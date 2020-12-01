from rest_framework import serializers
from core.models import Group, Student, MyUser


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    students = StudentSerializer(many=True)

    class Meta:
        model = Group
        fields = "__all__"

    def get_teacher(self, obj):
        return obj.teacher.username
