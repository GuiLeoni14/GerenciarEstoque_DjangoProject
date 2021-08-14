from django.forms import ModelForm
from produto.models import produto


class produtoForm(ModelForm):
    class Meta:
        model = produto
        fields = ['nome', 'tipo', 'descricao', 'fornecedor','quantidade', 'data']