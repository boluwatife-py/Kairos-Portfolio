from .models import Testimonial
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'who_you_are', 'rating', 'testimony', 'user_image']
        widgets = {
            'who_you_are': forms.TextInput(attrs={'placeholder': 'e.g. Music Producer'}),
        }