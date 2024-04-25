from django import forms
from .models import Message


class EmailMessageForm(forms.ModelForm):
    # name = forms.CharField(max_length=30, min_length=2, required=True, label='Name')
    # email = forms.EmailField(label='Email', required=True)
    # subject = forms.CharField(max_length=60, required=True, label='Subject')
    # message_text = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 7}), label='Message text')

    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message', ]
        widgets = {
            'message': forms.Textarea(attrs={'cols': 50,
                                             'rows': 7,
                                             'class': 'form-control'}),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message text'
        }