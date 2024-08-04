from django import forms
from .models import Venda, ItensVenda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente']

class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItensVenda
        fields = ['produto', 'quantidade']

ItemVendaFormSet = forms.inlineformset_factory(Venda, ItensVenda, form=ItemVendaForm, extra=1)
