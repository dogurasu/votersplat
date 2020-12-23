from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# using Django's generic views
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# request is supposed to be of type 'HttpRequest'
# def index(request: HttpRequest) -> HttpResponse:
#     latest_questions = Question.objects.order_by('-pub_date')[:5]
    
#     # template = loader.get_template('polls/index.html')
#     # context = {
#     #     'latest_question_list': latest_questions,
#     # }
#     # return HttpResponse(template.render(context, request))

#     # or
#     context = {'latest_question_list': latest_questions}
#     return render(request, 'polls/index.html', context)
    

# def detail(request: HttpRequest, question_id: int) -> HttpResponse:
#     # try:
#     #     question = Question.objects.get(pk = question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404(f"A question with the id {question_id} does not exist")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def vote(request: HttpRequest, question_id: int) -> HttpResponse:
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # redisplay question voting form
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # always return an HttpResponseRedirect after successfully dealing w/ POST data
#         # this prevents data from being posted twice if a user hits the Back button
#         # return HttpResponse(f"You're voting on question {question_id}"))
#         # return HttpResponse(reverse('polls:results', args=(question.id,)))
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def results(request: HttpRequest, question_id: int) -> HttpResponse:
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#     # return HttpResponse(f"You're looking at the results of question {question_id}")