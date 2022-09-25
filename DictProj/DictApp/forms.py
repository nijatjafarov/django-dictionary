from django import forms
from .models import Word, Translation, Definition

class CreateWordForm(forms.Form):
    name = forms.CharField(
        label='Əlavə edəcəyiniz sözü daxil edin (İngiliscə):',
        widget=forms.TextInput(attrs={'placeholder': 'Söz', 
        'style': 'width: 50%; min-width: 280px;'}),
        error_messages={
            'empty_value': "Boş dəyər daxil edilib.",
            'required': "Bu xana boş ola bilməz.",
            'invalid': "Yalnış dəyər daxil edilib.",
            'max_length': "Simvolların sayı maksimumu keçib.",
            'min_length': "Simvolların sayı minimumun altındadır."
            }
        )
    author_translation = forms.CharField(required=False,
        label='Özünüzün əlavə etmək istədiyiniz tərcümə (İstəyə görə):',
        widget=forms.TextInput(attrs={'placeholder': 'Tərcüməniz', 
        'style': 'width: 50%; min-width: 280px;'}),
        error_messages={
            'empty_value': "Boş dəyər daxil edilib.",
            'required': "Bu xana boş ola bilməz.",
            'invalid': "Yalnış dəyər daxil edilib.",
            'max_length': "Simvolların sayı maksimumu keçib.",
            'min_length': "Simvolların sayı minimumun altındadır."
            }
        )


    class Meta:
        model = Word
        fields = ['name','author_translation']

    def __init__(self, *args, **kwargs):
        super(CreateWordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.errors:
                visible.field.widget.attrs['class'] = 'form-control is-invalid'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
