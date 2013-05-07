from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from landing.models import Landing
from django.views.generic import CreateView
from landing.forms import LandingForm
from landing.models import Landing

#@csrf_exempt
#def custom_500_error_view(request):
#    return render_to_response("500.html", {}, context_instance=RequestContext(request))


class LandingCreateView(CreateView):
    form_class = LandingForm
    success_url = "/"
    template_name = "landing/landing.html"
    
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request,messages.SUCCESS,'Thank you!',extra_tags='alert alert-success')
        return HttpResponseRedirect('/')
    
