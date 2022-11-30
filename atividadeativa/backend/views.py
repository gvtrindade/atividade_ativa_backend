from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question

# Create your views here.
def index(req):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(req, 'backend/index.html', context)

def results(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(req, 'backend/results.html', context)

def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if req.method == 'POST':    
        selected_choice = question.option_set.get(pk=req.POST['option.text'])
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('backend:results', args=(question_id)))

    context = {'question': question}
    return render(req, 'backend/vote.html', context)
