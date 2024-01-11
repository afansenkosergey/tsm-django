from django.contrib.auth.models import User

from articles.models import Article
from django.test import TestCase
from django.urls import reverse


class ArticlesIndexPageTestCase(TestCase):

    def test_empty_database(self):
        response = self.client.get(reverse('articles:list'))
        self.assertContains(response, 'There are no articles')

    def test_multiple_articles_in_context(self):
        # Создаем несколько статей
        article1 = Article.objects.create(title='Article 1', text='Content 1', likes=50)
        article2 = Article.objects.create(title='Article 2', text='Content 2', likes=120)

        response = self.client.get(reverse('articles:list'))
        self.assertQuerysetEqual(
            response.context['articles'],
            [article1, article2],
            transform=lambda x: x
        )


# Пример тестов для страницы "articles:detail"

class ArticlesDetailPageTestCase(TestCase):

    def test_nonexistent_article_returns_404(self):
        response = self.client.get(reverse('articles:detail', args=[1000]))
        self.assertEqual(response.status_code, 404)

    def test_existing_article_contains_article_text(self):
        article = Article.objects.create(title='Existing Article', text='Article Content', likes=80)
        response = self.client.get(reverse('articles:detail', args=[article.id]))
        self.assertContains(response, 'Article Content')


# Добавление метода is_popular в модель Article и тесты для него

class ArticleModelTestCase(TestCase):

    def test_is_popular_returns_true_for_likes_over_100(self):
        article = Article.objects.create(title='Popular Article', text='Article Content', likes=120)
        self.assertTrue(article.is_popular())

    def test_is_popular_returns_false_for_likes_under_100(self):
        article = Article.objects.create(title='Normal Article', text='Article Content', likes=80)
        self.assertFalse(article.is_popular())

    def test_is_popular_returns_false_for_zero_likes(self):
        article = Article.objects.create(title='Unliked Article', text='Article Content', likes=0)
        self.assertFalse(article.is_popular())


class RegistrationAuthenticationTests(TestCase):
    def test_registration(self):
        response = self.client.post(reverse('articles:register'), {
            'username': 'test',
            'first_name': 'First',
            'last_name': 'Last',
            'email': 'test@example.com',
            'password1': 'test123test',
            'password2': 'test123test',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)

    def test_authentication(self):
        user = User.objects.create_user(username='test', password='test123')

        response = self.client.post(reverse('articles:login'), {
            'username': 'test',
            'password': 'test123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_add_article(self):
        user = User.objects.create_user(username='test', password='test123')
        self.client.login(username='test', password='test123')

        response = self.client.post(reverse('articles:add_article'), {
            'title': 'Test Article',
            'text': 'This is a test article.',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.count(), 1)
