from django import forms
# from core.fields import PhoneField
from core.models import Group, Student
from django.contrib.auth import get_user_model


class RegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.widgets.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password', 'password_confirm')
        widgets = {
            'password': forms.widgets.PasswordInput()
        }

    def clean_password_confirm(self):
        if self.cleaned_data['password_confirm'] != self.cleaned_data['password']:
            raise forms.ValidationError("Passwords do not match")
        return self.cleaned_data['password']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)

        user.set_password(self.cleaned_data['password'])
        user.save()

        return user


class ContactUS(forms.Form):
    title = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'students': forms.widgets.CheckboxSelectMultiple()
        }


class StudentForm(forms.ModelForm):
    # phone = PhoneField()

    class Meta:
        model = Student
        fields = '__all__'
