from django import forms
from .models import *

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('__all__')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

