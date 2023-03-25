from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'false')
    print(djtext)
    print(removepunc)
    if removepunc == 'on':
        punctuation = '''!@#$%^&*()_-{}|\][:"?><,./';'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuation', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")