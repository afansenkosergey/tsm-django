import json
import os
import sys

# Добавляем путь к каталогу проекта в sys.path
sys.path.append('/app')  # Замените '/app' на актуальный путь к вашему Django-проекту

# Настройка переменной окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from articles.models import Author, Article

# Открываем JSON-файл для чтения
with open('add_to_db/articles.json', 'r') as file:
    data = json.load(file)

# Создаем авторов и статьи
for author_data in data['authors']:
    author = Author.objects.create(
        first_name=author_data['first_name'],
        last_name=author_data['last_name'],
        date_of_birth=author_data.get('date_of_birth')
    )

for article_data in data['articles']:
    # Создаем статью
    article = Article.objects.create(
        title=article_data['title'],
        text=article_data['text'],
        pub_date=article_data['pub_date'],
        likes=article_data['likes'],
    )

    # Добавляем авторов к статье
    for author_id in article_data['authors']:
        author = Author.objects.get(pk=author_id)
        article.authors.add(author)

    # Сохраняем изменения
    article.save()

print('Объекты успешно созданы.')

