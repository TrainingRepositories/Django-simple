from django import forms
from .models import Books , Authors , Shelves


class BooksForm(forms.ModelForm):
    class Meta():
        model = Books
        fields = '__all__'
    
class AuthorsForm(forms.ModelForm):
    class Meta():
        model = Authors
        fields = '__all__'
        
class ShelvesForm(forms.ModelForm):
    class Meta():
        model = Shelves
        fields = '__all__'
    


