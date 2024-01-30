from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.request import Request

from api.filters import ChoiceCountFilter
from api.serializer import ArticleSerializer, CategorySerializer, ProductSerializer, ChoiceSerializer, \
    QuestionSerializer
from articles.models import Article
from polls.models import Question, Choice
from shop.models import Category, Product


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('id')
    serializer_class = ArticleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, ChoiceCountFilter]
    ordering_fields = ['id', 'question_text', 'pub_date']
    search_fields = ['id', 'question_text', 'pub_date']


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all().order_by('id')
    serializer_class = ChoiceSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['id', 'choice']
    search_fields = ['id', 'choice']


@api_view(['POST'])
def choice_vote(request: Request, question_id: int):
    question = get_object_or_404(Question, id=question_id, pub_date__lte=timezone.now())
    selected_choice = get_object_or_404(question.choices, id=request.data['choice'])
    selected_choice.votes += 1
    selected_choice.save()
    return redirect('api:question-detail', question_id)
