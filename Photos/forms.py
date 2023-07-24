from django import forms
from .models import Shot
from .models import Category

class FormAddPhoto(forms.ModelForm):
    class Meta:
        model = Shot
        choices = Category.objects.all().values_list('category_name', 'category_name')
        choices = [('a', 'a'), ('b', 'b')]
        choice_list = [item for item in choices]

        fields = ['image', 'category', 'title']
        widgets = {
            "title": forms.TextInput(attrs={'placeholder':'The title' }),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }



class FormAddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
        widgets = {
            'category_name': forms.TextInput(attrs={'placeholder':'Enter one word' })
        }