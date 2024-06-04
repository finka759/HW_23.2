from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def check_stop_words(self, cleaned_data):
        for stop_word in self.stop_words:
            if stop_word in cleaned_data:
                raise forms.ValidationError(f'Нельзя использовать слово "{stop_word}"')
        return cleaned_data

    def clean_product_name(self):
        cleaned_data = self.cleaned_data["product_name"]
        return self.check_stop_words(cleaned_data)

    def clean_product_description(self):
        cleaned_data = self.cleaned_data["product_description"]
        return self.check_stop_words(cleaned_data)


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
