from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_categories_from_cache():
    """ Получает категории продуктов из кеша, если кеш пуст получает из БД и записывает в кеш"""
    if not CACHE_ENABLED:
        return Category.objects.all()


    key = 'category_list'  # Создаем ключ для хранения
    category_list = cache.get(key)  # Пытаемся получить данные
    if category_list is None:
        # Если данные не были получены из кеша, то выбираем из БД и записываем в кеш
        category_list = Category.objects.all()
        cache.set(key, category_list)
    return category_list
