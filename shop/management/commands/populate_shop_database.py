import json
from django.core.management.base import BaseCommand
from shop.models import Category, Product


class Command(BaseCommand):
    help = 'Populate the shop database with initial data from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('--data_file_path', type=str, help='Path to the JSON file with initial data')

    def handle(self, *args, **options):
        data_file_path = options.get('data_file_path', 'default_data.json')

        try:
            with open(data_file_path, 'r') as file:
                data = json.load(file)

                categories_data = data.get('categories', [])
                for category_data in categories_data:
                    Category.objects.create(**category_data)

                products_data = data.get('products', [])
                for product_data in products_data:
                    category_name = product_data.pop('category')
                    category = Category.objects.get(name=category_name)
                    Product.objects.create(category=category, **product_data)

                self.stdout.write(self.style.SUCCESS('Successfully populated the shop database'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {data_file_path}'))

        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR(f'Error decoding JSON file: {data_file_path}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
