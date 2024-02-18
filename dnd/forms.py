from django import forms

from .models import NonPlayerCharacter

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class NewCharacterForm(forms.ModelForm):
    class Meta:
        model = NonPlayerCharacter
        fields = ('name', 'race','affiliation','height', 'age', 'description', 'image',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'age': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'height': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'affiliation': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'race': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }