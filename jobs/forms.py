from django import forms


class JobApplicationForm(forms.Form):
    E_TYPE  = (
        (None, '--pleace choose --'), 
        ('full-time', 'Full-time'), 
        ('part-time', 'Part-time'),
        ('contract work', 'Contract work')
    )
    DAYS_WORK = (
        ('MON' ,'MON'),('TUE','TUE'),('WED','WED'),('THU','FRI')
    )

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(initial='https://',required=False)
    employment_type = forms.ChoiceField(choices=E_TYPE,required=True)
    start_date = forms.DateField(help_text='The earliest date you can start working.')
    available_days = forms.MultipleChoiceField(choices = DAYS_WORK ,required=True, help_text='Select all days that you can work.')
    desired_hourly_wage = forms.DecimalField()
    cover_letter = forms.CharField()
    confirmation = forms.BooleanField(label='I certify that the information I have provided is true.', required=True)