from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(req, 'backend/index.html')

def results(req):
    return render(req, 'backend/results.html')

def vote(req):
    return render(req, 'backend/vote.html')