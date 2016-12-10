from django.conf import settings
from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.is_anonymous():
        context = {'IS_PRODUCTION': settings.IS_PRODUCTION}
        return render(request, 'discovery/index.html', context=context)
    if request.user.email:
        return render(request, 'discovery/rate.html')
    return render(request, 'auth_disco/provide_email.html')