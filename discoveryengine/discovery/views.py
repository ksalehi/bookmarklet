from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.is_anonymous():
        return render(request, 'discovery/index.html')
    return render(request, 'discovery/rate.html')