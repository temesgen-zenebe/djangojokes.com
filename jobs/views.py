import html
from pyexpat import model
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from common.utils.email import send_email
from .forms import JobApplicationForm
from .models import Applicant

# Create your views here.

class JobAppView(CreateView):
    model = Applicant
    template_name = 'jobs/applicant_form.html'
    form_class = JobApplicationForm
    success_url = reverse_lazy('jobs:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'egolebearingplc@gmail.com'
        subject = 'Application for Joke Writer'
        content = f'''<p>Hey HR Manager!</p>
            <p>Job application received:</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)

class JobAppThanksView(TemplateView):
    template_name = 'jobs/thanks.html'
