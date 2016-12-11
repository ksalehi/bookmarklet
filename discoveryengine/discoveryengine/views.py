from django.conf import settings
from django.contrib.auth import logout as lo
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if request.user.is_anonymous():    
        context = {'IS_PRODUCTION': settings.IS_PRODUCTION, 'next': '/'}
        # If there are query params, they should be in the NEXT login redirect
        if request.GET:
            context['next'] = context['next']+'?'+request.GET.urlencode()
        # If the query param is a DOI, they should go to the anonymous rate page
        if request.GET.get('doi', None):
            return render(request, 'discovery/rate_anonymous.html', context=context)
        # Go to index to login!
        return render(request, 'discovery/index.html', context=context)

    # If the user has an email, they can rate!
    if request.user.email:
        return render(request, 'discovery/rate.html')

    # We need emails, so please oblige
    return render(request, 'auth_disco/provide_email.html')

def logout(request):
    lo(request)
    return redirect('/')