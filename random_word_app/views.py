from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def random_word(request):
    request.session['word'] = get_random_string(length=14) 
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    return render(request, 'index.html')

def reset(request):
    request.session.clear()
    return redirect('/')