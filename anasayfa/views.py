from django.shortcuts import render, HttpResponse


# Create your views here.
def anasayfa_view(request):
    return render(request, 'anasayfa.html', {})
