from django.core.cache import cache
from catalog.models import Category

def get_cached_categories():
    """
    Функция для получения списка категорий с кешированием.
    """
    categories = cache.get('categories_list')

    if not categories:
        categories = Category.objects.all()
        cache.set('categories_list', categories, 60 * 30)  # Кешируем на 30 минут

    return categories