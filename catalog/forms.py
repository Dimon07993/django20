from django import forms
from prompt_toolkit.validation import ValidationError

from .models import Product, Version

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', 'хрен']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'



class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'image', 'price')


    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if any(word in cleaned_data.lower() for word in FORBIDDEN_WORDS):
            raise forms.ValidationError('Название не должно содержать запрещенные слова.')
        return cleaned_data


    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        if any(word in cleaned_data.lower() for word in FORBIDDEN_WORDS):
            raise forms.ValidationError('Описание не должно содержать запрещенные слова.')
        return cleaned_data



class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'version_number', 'version_name', 'is_current')
