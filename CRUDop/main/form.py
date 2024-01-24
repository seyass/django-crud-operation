from django.forms import ModelForm
from . models import my_user

class adminUser(ModelForm):
    class Meta:
        model = my_user
        fields = '__all__'