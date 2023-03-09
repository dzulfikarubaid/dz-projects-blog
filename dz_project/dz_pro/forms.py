from django import forms
from .models import Post

class WriteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('first_name','last_name','title','body','category')
        widgets = {
            # 'author' : forms.Select(attrs={'class':'form author'}),
            'first_name': forms.TextInput(attrs={'class':'form first'}),
            'last_name' : forms.TextInput(attrs={'class':'form last'}),
            'title' : forms.TextInput(attrs={'class':'form title'}),
            'body' : forms.TextInput(attrs={'class':'form body'}),
            'category' : forms.TextInput(attrs={'class':'form category'})
        }