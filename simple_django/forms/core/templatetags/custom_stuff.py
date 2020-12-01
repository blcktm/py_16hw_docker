from django import template
from core.models import MyUser
import random

register = template.Library()


@register.filter
def mass_filter(mass):
    vars = []
    for var in mass:
        if var % 2 == 0:
            if var != 0:
                vars.append(var)
    return vars


@register.filter
def countw_filter(str):
    return len(str.split())


# @register.simple_tag
# def random_teachers():
#     teachers = MyUser.objects.all()
#     objects_count = MyUser.objects.count() - 1
#     rand_teachers = []
#     for i in range(5):
#         rand_teachers.append(teachers[(random.randint(0, objects_count))])
#     return {
#         'teachers': rand_teachers
#     }
