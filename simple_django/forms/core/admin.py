from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import Student, Group, Logger, MyUser, Currency


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'phone', )
    search_fields = ('last_name', )
    list_filter = ('group', )


class LoggerAdmin(admin.ModelAdmin):
    list_display = ('time_created', 'request_path', 'request_method', 'execution_time')


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')}),
        (('Personal info'), {
            'fields': ('first_name', 'last_name')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {
            'fields': ('last_login', 'date_joined')}),
    )


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('ccy', 'buy_price', 'sell_price', 'title', 'created')


admin.site.register(Group, )
admin.site.register(Student, StudentAdmin)
admin.site.register(Logger, LoggerAdmin)
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Currency, CurrencyAdmin)
