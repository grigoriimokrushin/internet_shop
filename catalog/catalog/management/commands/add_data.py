from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all = []
        categories_list = [
            {"name": "Для детей", "description": "То во что играют дети."},
            {"name": "Для рыбалки", "description": "То что берут на рыбалку."},
        ]

        for category in categories_list:
            Category.objects.create(**category)
