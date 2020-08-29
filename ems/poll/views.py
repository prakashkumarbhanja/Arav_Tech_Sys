from django.shortcuts import render
from django.http import Http404, HttpResponse

from poll.models import Question, Choice, Answer
from django.contrib.auth.models import User

def index(request): #13

    questions = Question.objects.all()
    context = {"questions": questions}
    template = 'poll/index.html'
    return render(request, template, context)

def details(request, id):

    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
    context = {"question": question}
    template = 'poll/details.html'
    return render(request, template, context)


def poll(request, id):
    if request.method == 'GET':
        print(request)
        try:
            question = Question.objects.get(id=id)
        except:
            raise Http404

        context = {"question": question}
        template = 'poll/poll.html'
        return render(request, template, context)

    if request.method == 'POST':

        user_id = 1
        choice = request.POST['choice']
        answe_created = Answer.objects.create(user_id = user_id, choice_id=choice)
        if answe_created:
            return HttpResponse("You have voted Successfully")
        else:
            return HttpResponse("You have not voted Successfully")
