import json
import os
import sys

# Добавляем путь к каталогу проекта в sys.path
sys.path.append('/app')  # Замените '/app' на актуальный путь к вашему Django-проекту

# Настройка переменной окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from shop.models import Category, Product


with open('add_to_db/shop.json', 'r') as file:
    data = json.load(file)

# Создаем категории
for category_data in data['categories']:
    category = Category.objects.create(
        id=category_data['id'],
        name=category_data['name']
    )

# Создаем продукты
for product_data in data['products']:
    product = Product.objects.create(
        name=product_data['name'],
        description=product_data['description'],
        price=product_data['price'],
        category_id=product_data['category_id']
    )


print('Объекты успешно созданы.')