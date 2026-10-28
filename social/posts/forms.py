from django import forms
from .models import Post

class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('description', 'picture')
        widgets = {
            'description': forms.Textarea({
                'style': 'height: 150px; margin-bottom: 30px;',
                'id': 'input2',
                'rows': 4
            }),
            'picture': forms.FileInput()
        }
    def clean_description(self):
        description = self.cleaned_data.get('description')

        if len(description) > 100:
            raise forms.ValidationError("Description shouldn't get to 100 characters")

        return description