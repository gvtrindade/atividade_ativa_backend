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
        try:
            print('Recuperando opção')
            print(req.POST)
            selected_choice = question.option_set.get(pk=(int(req.POST['option']) + 1))
        except KeyError:
            print('Erro')
            return render(req, 'backend/vote.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            print('Sucesso')
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('backend:results', args=(question_id,)))
    else:
        context = {'question': question}
        return render(req, 'backend/vote.html', context)
