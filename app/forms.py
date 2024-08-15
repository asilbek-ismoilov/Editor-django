from django.forms import ModelForm
from django import forms
from .models import Contact, Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        
        fields = ['full_name','email','message']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get('name')
        message = cleaned_data.get('message')
        
        if name:
            if len(name) < 3:
                self.add_error('name', "Minimum 3 characters required")
        else:
            self.add_error('name', "Name is required")

        if not message:
            self.add_error('message', "Message is required")

        return cleaned_data
