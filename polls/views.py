from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.cache import cache_page
from .forms import QuestionForm
from .models import Question, Choice



def index(request: HttpResponse):
    questions = Question.objects.filter(pub_date__lte=timezone.now())
    context = {'latest_question_list': questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id: int):
    question = get_object_or_404(Question, pk=question_id, pub_date__lte=timezone.now())
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def vote(request, question_id: int):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'error_message': "You didn't select a choice.",
            'question': question,
        })
    selected_choice.votes += 1
    selected_choice.save()
    return redirect('polls:results', question_id)


def results(request, question_id: int):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)


def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data['question_text']
            pub_date = form.cleaned_data['publication_date']
            question = Question(question_text=question_text, pub_date=pub_date)
            for choice_text in form.cleaned_data['choices'].split('\n'):
                question.choices.create(choice_text=choice_text, votes=0)
            return render('polls:detail', question.id)
    else:
        form = QuestionForm()
    return render(request, 'polls/create_question.html', {'form': form})


def category_list(request):
    return None
