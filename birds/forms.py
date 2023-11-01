from django import forms

from birds.models import Birds


class StyleFormMixin:  # Данный класс создан для замешивания стилей в форму
    def __init__(self, *args, **kwargs):  # Функция, которая делает вывод карточки на экран более привлекательным
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class BirdForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Birds
        fields = '__all__'
