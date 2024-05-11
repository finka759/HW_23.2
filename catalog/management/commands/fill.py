import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    @staticmethod
    def json_read_categories(data_from_file):
        category_list = []
        for item in data_from_file:
            if item.get('model') == 'catalog.category':
                category_list.append(item)
        return category_list

    @staticmethod
    def json_read_products(data_from_file):
        product_list = []
        for item in data_from_file:
            if item.get('model') == 'catalog.product':
                product_list.append(item)
        return product_list

    def handle(self, *args, **options):
        print('Hi Sky')
        with open('db.json', encoding='utf-8') as file:
            data_from_file = json.load(file)

        # Удалите все продукты
        Category.objects.all().delete()
        # Сброс индефикатора Category
        Category.truncate_table_restart_id()
        # Удалите все категории
        Product.objects.all().delete()

        category_for_create = []
        product_for_create = []

        for category in Command.json_read_categories(data_from_file):
            category_for_create.append(
                Category(pk=category.get('pk'),
                         category_name=category.get('fields').get('category_name'),
                         category_description=category.get('fields').get('category_description'))
            )


        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products(data_from_file):
            product_for_create.append(
                Product(pk=product.get('pk'),
                        product_name=product.get('fields').get('product_name'),
                        product_description=product.get('fields').get('product_description'),
                        product_image=product.get('fields').get('product_image'),
                        product_category=Category.objects.get(pk=product.get('fields').get('product_category')),
                        product_created_at=product.get('fields').get('product_created_at'),
                        product_updated_at=product.get('fields').get('product_updated_at'),
                        product_pay_for_sail=product.get('fields').get('product_pay_for_sail')
                        )
            )


        Product.objects.bulk_create(product_for_create)
