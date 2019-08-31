from django.forms import ModelForm
from website.models import Veiculos

class FormVeiculo(ModelForm):
    class Meta:
        model = Veiculos
        fields = '__all__'
