from django.http import Http404
from django.shortcuts import render

# Create your views here.
def analytics(request):
    if request.user.is_staff or request.user.is_superuser:
        return render(request, 'internal/analytics.html')
    else:
        raise Http404