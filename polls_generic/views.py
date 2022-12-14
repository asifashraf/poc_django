from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    '''the ListView generic view uses a default template called <app name>/<model name>_list.html; 
    we use template_name to tell ListView to use our existing "polls/index.html" template.'''
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    '''By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html. 
    In our case, it would use the template "polls/question_detail.html". 
    The template_name attribute is used to tell Django to use a specific template name instead of the autogenerated default template name. 
    We also specify the template_name for the results list view – 
    this ensures that the results view and the detail view have a different appearance when rendered, even though they’re both a DetailView behind the scenes.'''


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls_generic/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls_generic:results', args=(question.id,)))
