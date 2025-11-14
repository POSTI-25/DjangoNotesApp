from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(),
            'text': forms.Textarea(attrs={'class': 'form-control my-3'}),
        }
        labels = {
            'text': 'Write your notes'
        }


    def clean_title(self):
        title = self.cleaned_data[('title')]
        if not title or not title.strip():
            raise forms.ValidationError("Title cannot be empty.")
        return title