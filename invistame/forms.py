from django.forms import ModelForm
from .models import Investimento

class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        fields = "__all__"  # Inclui todos os campos do modelo Investimento
        