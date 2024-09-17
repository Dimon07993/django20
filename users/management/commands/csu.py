from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email = "admin@csu",
            password = "admin",
            is_staff = True,
            is_superuser = True
        )

        user.set_password("admin")
        user.save()