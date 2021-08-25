from django import  forms
from apps.core.models import Newsletter

class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Enter your email',"class":"form-control"}))

    class Meta:
        model=Newsletter
        fields =['email']