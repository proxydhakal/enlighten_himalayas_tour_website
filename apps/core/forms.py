from django import  forms
from apps.core.models import Newsletter, Contact
from django.forms import  TextInput,Textarea
from django.forms import fields
class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Enter your email',"class":"form-control"}))

    class Meta:
        model=Newsletter
        fields =['email']

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('email', 'name','subject','message')
        widgets ={
            'email':TextInput(attrs={'class':'form-control'}),
            'name':TextInput(attrs={'class':'form-control'}),
            'subject':TextInput(attrs={'class':'form-control'}),
            'message':Textarea(attrs={'class':'form-control'}),
        }