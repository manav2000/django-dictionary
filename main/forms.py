from django import forms


class SearchForm(forms.Form):
    word = forms.CharField(max_length=300, widget=forms.TextInput(
        attrs={
            'class': 'search-field form-control',
            'placeholder': 'Enter a word',
        }
    ))
