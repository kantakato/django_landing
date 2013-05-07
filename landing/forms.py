from django.forms import ModelForm
from landing.models import Landing

class LandingForm(ModelForm):
    class Meta:
        model = Landing