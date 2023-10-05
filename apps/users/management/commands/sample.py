from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Create sample data for testing"

    def create_superuser(self, name, username, email, password):
        users = User.objects.filter(email=email)
        num = len(users)
        if num:
            print('User: ' + email + 'password: ' + password + ' ' + 'already exists')
            return

        User.objects.create_user(
            name=name,
            username=username,
            email=email,
            password=password,
            is_superuser=True,
            is_active=True,
            is_staff=True,

        )
        print('User: ' + email + ' password: ' + password)

    def handle(self, *args, **kwargs):
        self.create_superuser(
            username='shohel',
            name='Shohel Rana',
            password='shohel-22',
            email='shohel@devxhub.com',
        )
        self.create_superuser(
            username='hadisur',
            name='Hadisur Rahman',
            password='hadisur-22',
            email='hadis@devxhub.com',
        )
        self.create_superuser(
            username='eliyas',
            name='Eliyas Hossain',
            password='eliyas-74',
            email='eliyas@devxhub.com',
        )
        self.create_superuser(
            username='anik12',
            name='Anik Muktadir',
            password='admin',
            email='admin@gmail.com',
        )
        self.create_superuser(
            username='foysal',
            name='Mohammad Foysal',
            password='foysal',
            email='foysal.devxhub@gmail.com',
        )

        print('Superuser created successfully')


# python manage.py sample
