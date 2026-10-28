from django import forms
from .models import Global_Chat
class GlobalChatForm(forms.ModelForm):
    class Meta:
        model = Global_Chat
        fields = ('messages',)
        widgets = {
            'messages': forms.TextInput({
                'id': 'main_input'
            })
        }