from django import forms

PRODUCT_QUANTITY_OPTIONS = [(i, str(i)) for i in range(1, 100)]

class AddProductToCartForm(forms.Form):
    
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_OPTIONS, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    