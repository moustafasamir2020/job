from django import forms
from . models import apply,job

class apply_form (forms.ModelForm):
    class Meta:
        model = apply
        fields = "__all__"
        exclude = ('job',)


class Jobform (forms.ModelForm):
    class Meta :
        model = job
        fields = '__all__'
        exclude = ('owner','slug')
        