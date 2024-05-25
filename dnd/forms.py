from django import forms

from .models import NonPlayerCharacter, Character_Sheet

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

class CharacterSheet(forms.ModelForm):
    class Meta:
        model = Character_Sheet
        fields = ('character_name','lvl','hp','str','dex','con','int','wis','cha','ac','speed','special_item','special_item2','special_item3','special_item4','special_item5','special_item6','special_item7',)

        widgets = {
            'character_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'lvl': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'hp': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'str': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'dex': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'con': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'int': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'wis': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'cha': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'ac': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'speed': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'special_items': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'special_items2': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'special_items3': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'special_items4': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'special_items5': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'special_items6': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'special_items7': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
        }