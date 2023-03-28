from django import forms
from .models import FeedBack

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'
        labels = {
            'name': 'Ваше имя',
            'email': 'Ваша почта',
            'feedback': 'Жалобы или предложения',
        }
        error_messages = {
            'name': {
                'max_length': 'Cлишком много символов',
                'min_length': 'Cлишком мало символов',
                'required': 'Это поле не должно быть пустым'
            },
            'email': {
                'max_length': 'Cлишком много символов',
                'min_length': 'Cлишком мало символов',
                'required': 'Это поле не должно быть пустым'
            },
            'feedback': {
                'max_length': 'Cлишком много символов',
                'min_length': 'Cлишком мало символов',
                'required': 'Это поле не должно быть пустым'
            }
        }