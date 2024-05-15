'''from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'quantidade', 'preco_compra', 'preco_venda', 'preco_marketing_promocional', 'descricao_curta','slug']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'Nome do Produto', 'class': 'form-control form-control-lg'}),
            'quantidade': forms.TextInput(attrs={'placeholder':'Quantidade', 'class': 'form-control form-control-lg'}),
            'descriao': forms.Textarea(attrs={'placeholder':'Descricao', 'class': 'form-control form-control-lg'}),
            'preco_compra': forms.TextInput(attrs={'placeholder':'Preco compra', 'class': 'form-control form-control-lg'}),
            'preco_venda': forms.TextInput(attrs={'placeholder':'Preco venda', 'class': 'form-control form-control-lg'}),
            'preco_promocional': forms.TextInput(attrs={'placeholder':'Preco promocional', 'class': 'form-control form-control-lg'}),
        }'''