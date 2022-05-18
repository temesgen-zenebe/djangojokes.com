from datetime import datetime
from django import forms 
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_future_date(value):
    if value < datetime.now().date():
        raise ValidationError(
            message=f'{value} is in the past.', code='past_date'
        )
    
class JobApplicationForm(forms.Form):
    E_TYPE  = (
        (None, '--pleace choose --'), 
        ('full-time', 'Full-time'), 
        ('part-time', 'Part-time'),
        ('contract work', 'Contract work')
    )
    DAYS_WORK = (
        (1 ,'MON'),(2,'TUE'),(3,'WED'),(4,'FRI')
    )
    YEARS = range(datetime.now().year, datetime.now().year+2)

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                #'class': 'form-control',
                'autofocus': True
            }
        )
    )
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(
            required=False,
            widget=forms.URLInput(
                attrs={
                    #'class': 'form-control',
                    'placeholder': 'https://www.example.com',
                    'size': '50'
                }
                
            ),
            validators=[URLValidator(schemes=['http', 'https'])]
            
    )
    employment_type = forms.ChoiceField(choices=E_TYPE,required=True)
    start_date = forms.DateField(
        help_text='The earliest date you can start working.',
        required=False,
        widget=forms.SelectDateWidget(
            attrs={'style': 'width: 31%; display: inline-block; margin: 0 1%'},
            years=YEARS,
            #empty_label=("Choose Year", "Choose Month", "Choose Day"),  
            
        ),
        validators=[validate_future_date],
        error_messages = {'past_date': 'Please enter a future date.'}
    
    )
    available_days = forms.TypedMultipleChoiceField(
        choices = DAYS_WORK ,
        coerce=int,
        required=True, 
        help_text='Select all days that you can work.',
        widget=forms.CheckboxSelectMultiple(
            attrs={'checked':True}, 
        )
    )
    desired_hourly_wage = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={'min': '10.00', 'max': '100.00','step': '.25'}
        )
    )
    cover_letter = forms.CharField()
    confirmation = forms.BooleanField(label='I certify that the information I have provided is true.', required=True)