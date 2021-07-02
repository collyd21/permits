from django import forms
from .models import Mewp


class MewpForm(forms.ModelForm):
    class Meta:
        model = Mewp
        fields = ('make_model', 'sn_no', 'inspected_by', 'location', 'date', 'question_1', 'question_2', 'question_3', 'question_4', 'question_5', 'question_6', 'question_7', 'question_8', 'question_9', 'question_10', 'question_11', 'question_12', 'question_13', 'question_14', 'question_15', 'question_16', 'question_17', 'question_18', 'question_19', 'question_20','comments',)
        widgets = {
            'question_1': forms.RadioSelect,
            'question_2': forms.RadioSelect,
            'question_3': forms.RadioSelect,
            'question_4': forms.RadioSelect,
            'question_5': forms.RadioSelect,
            'question_6': forms.RadioSelect,
            'question_7': forms.RadioSelect,
            'question_8': forms.RadioSelect,
            'question_9': forms.RadioSelect,
            'question_10': forms.RadioSelect,
            'question_11': forms.RadioSelect,
            'question_12': forms.RadioSelect,
            'question_13': forms.RadioSelect,
            'question_14': forms.RadioSelect,
            'question_15': forms.RadioSelect,
            'question_16': forms.RadioSelect,
            'question_17': forms.RadioSelect,
            'question_18': forms.RadioSelect,
            'question_19': forms.RadioSelect,
            'question_20': forms.RadioSelect,
        }