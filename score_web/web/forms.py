from django import forms
from .models import Score,Memo,Media

class EditScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['title']
        
class EditMemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['document', 'titles']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class EditMediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['mediapath', 'comment', 'titles']