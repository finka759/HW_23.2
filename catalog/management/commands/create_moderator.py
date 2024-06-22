from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда для создания суперпользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email='moderator',
            is_active=True,
        )

        user.set_password('moderator')
        user.save()
