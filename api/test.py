from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from articles.models import Article, Author
from polls.models import Question
from shop.models import Category, Product


class QuestionViewTest(TestCase):
    def test_empty_question_list(self):
        response = self.client.get('/api/questions/')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['count'], 0)
        self.assertEqual(data['next'], None)
        self.assertEqual(data['previous'], None)
        self.assertEqual(data['results'], [])

    def test_question_list(self):
        Question.objects.create(question_text='Text1', pub_date=timezone.now())
        Question.objects.create(question_text='Text2', pub_date=timezone.now())

        response = self.client.get('/api/questions/')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['count'], 2)
        self.assertEqual(len(data['results']), 2)
        self.assertEqual(data['results'][0]['question_text'], 'Text1')
        self.assertEqual(data['results'][1]['question_text'], 'Text2')

    def test_nonexistent_question_detail(self):
        response = self.client.get('/api/questions/1/')
        self.assertEqual(response.status_code, 404)

    def test_question_detail(self):
        question = Question.objects.create(question_text='Text1', pub_date=timezone.now())

        response = self.client.get(f'/api/questions/{question.id}/')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['question_text'], question.question_text)


class ArticleViewTest(TestCase):
    def test_empty_article_list(self):
        response = self.client.get('/api/article/')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['count'], 0)
        self.assertEqual(data['next'], None)
        self.assertEqual(data['previous'], None)
        self.assertEqual(data['results'], [])

    def test_article_list(self):
        Article.objects.create(title='Статья1', text='Содержание1')
        Article.objects.create(title='Статья2', text='Содержание2')

        response = self.client.get('/api/article/')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['count'], 2)
        self.assertEqual(len(data['results']), 2)
        self.assertEqual(data['results'][0]['title'], 'Статья1')
        self.assertEqual(data['results'][1]['title'], 'Статья2')

    def test_nonexistent_article_detail(self):
        response = self.client.get('/api/article/1/')
        self.assertEqual(response.status_code, 404)

    def test_article_detail(self):
        article = Article.objects.create(title='Статья1', text='Содержание1')

        response = self.client.get(f'/api/article/{article.id}/')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['title'], article.title)
        self.assertEqual(data['text'], article.text)

    # Тесты для запросов POST, PUT, DELETE

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(first_name='Test', last_name='Author')

    def test_create_article(self):
        data = {
            'title': 'Новая статья',
            'text': 'Содержание новой статьи',
            'user': self.user.id,
            'authors': [self.author.id]
        }
        response = self.client.post('/api/article/', data)
        self.assertEqual(response.status_code, 201)

        created_article = Article.objects.filter(title='Новая статья').first()
        self.assertIsNotNone(created_article)
        self.assertEqual(created_article.text, 'Содержание новой статьи')

    def test_update_article(self):
        article = Article.objects.create(title='Статья', text='Содержание', user=self.user)
        updated_data = {
            'title': 'Обновленная статья',
            'text': 'Обновленное содержание',
            'user': self.user.id,
            'authors': [self.author.id]
        }
        response = self.client.put(f'/api/article/{article.id}/', updated_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        updated_article = Article.objects.get(id=article.id)
        self.assertEqual(updated_article.title, 'Обновленная статья')
        self.assertEqual(updated_article.text, 'Обновленное содержание')

    def test_delete_article(self):
        article = Article.objects.create(title='Статья', text='Содержание', user=self.user)
        response = self.client.delete(f'/api/article/{article.id}/')
        self.assertEqual(response.status_code, 204)


class CategoryViewTest(TestCase):
    def test_empty_category_list(self):
        response = self.client.get('/api/category/')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['count'], 0)
        self.assertEqual(data['next'], None)
        self.assertEqual(data['previous'], None)
        self.assertEqual(data['results'], [])

    def test_category_list(self):
        Category.objects.create(name='Категория1')
        Category.objects.create(name='Категория2')

        response = self.client.get('/api/category/')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['count'], 2)
        self.assertEqual(len(data['results']), 2)
        self.assertEqual(data['results'][0]['name'], 'Категория1')
        self.assertEqual(data['results'][1]['name'], 'Категория2')

    def test_nonexistent_category_detail(self):
        response = self.client.get('/api/category/1/')
        self.assertEqual(response.status_code, 404)

    def test_category_detail(self):
        category = Category.objects.create(name='Категория1')

        response = self.client.get(f'/api/category/{category.id}/')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['name'], category.name)


class ProductsViewTest(TestCase):
    def test_empty_products_list(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['count'], 0)
        self.assertEqual(data['next'], None)
        self.assertEqual(data['previous'], None)
        self.assertEqual(data['results'], [])

    def test_products_list(self):
        category = Category.objects.create(name='Категория1')

        Product.objects.create(name='Продукт1', description='Описание', price=10.99, category=category)
        Product.objects.create(name='Продукт2', description='Описание', price=20.99, category=category)

        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['count'], 2)
        self.assertEqual(len(data['results']), 2)
        self.assertEqual(data['results'][0]['name'], 'Продукт1')
        self.assertEqual(data['results'][1]['name'], 'Продукт2')

    def test_nonexistent_product_detail(self):
        response = self.client.get('/api/products/1/')
        self.assertEqual(response.status_code, 404)

    def test_product_detail(self):
        category = Category.objects.create(name='Категория1')
        product = Product.objects.create(name='Продукт2', description='Описание', price=20.99, category=category)

        response = self.client.get(f'/api/products/{product.id}/')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['name'], product.name)
        self.assertEqual(data['description'], product.description)
        self.assertEqual(data['price'], str(product.price))
        self.assertEqual(data['category'], product.category.id)
