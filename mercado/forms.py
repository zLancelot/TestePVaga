from django.forms import ModelForm
from mercado.models import Venda


class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = ['id_cliente', 'id_vendedor', 'id_produto']