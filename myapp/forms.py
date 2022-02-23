from django import forms
from django.forms import ModelForm
from .models import Flower


# With ModelForm we don’t need to specify the fields again. We already add the
# fields in the Flower model
#
# ModelForm is a helper class that creates that Form class from a Model
# Like for edit page we need a table so we use the Flower table with django Model form
class MyForm(ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', widget = forms.Textarea(attrs={'class': 'form-control '}))

    # Adding CSS class for Bootstrap,we wanted to add the form-control CSS
    # class to the title input element

    # Model Meta is basically the inner class of your model class. Model Meta is basically used to change the
    # behavior of your model fields like changing order options,verbose_name and lot of other options. It's
    # completely optional to add Meta class in your model

    class Meta:
        model = Flower
        fields = ['title','description']  # Recommended to use all fields otherwise unintentionally expose the fields
