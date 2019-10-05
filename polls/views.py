from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Question

# Create your views here.

def index(request):
    latest_questions_list = Question.objects.order_by("-pub_date")[:5]
    # output = ', '.join([q.question_text for q in latest_questions_list])
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_questions_list': latest_questions_list,
    }
    return render(request, 'polls/index.html', context)# HttpResponse(template.render(context, request))

def detail(request, question_id):
    """try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")"""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def result(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse(f'You\'re voting on question {question_id}')




