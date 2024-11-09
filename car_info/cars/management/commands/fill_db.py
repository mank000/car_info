import csv
import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from cars.models import Car, Comment

User = get_user_model()


class Command(BaseCommand):
    help = 'Импорт данных из CSV файлов в базу данных'

    def handle(self, *args, **kwargs):
        base_dir = os.path.join(settings.STATICFILES_DIRS[0], 'data')

        self.import_users(os.path.join(base_dir, 'users.csv'))

        self.import_cars(os.path.join(base_dir, 'cars.csv'))

        self.import_comments(os.path.join(base_dir, 'comments.csv'))

        self.stdout.write(
            self.style.SUCCESS('Все данные успешно импортированы!'))

    def import_users(self, csv_file_path):
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(
                csv_file, delimiter=',',
                fieldnames=[
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "password",
                    "is_staff",
                    "is_active",
                ])

            for row in csv_reader:
                try:
                    User.objects.create(
                        username=row['username'],
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        email=row['email'],
                        password=row['password'],
                        is_staff=row['is_staff'],
                        is_active=row['is_active'],
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f'Ошибка при сохранении пользователя: {e}')
                    )

    def import_cars(self, csv_file_path):
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(
                csv_file, delimiter=',',
                fieldnames=[
                    "make",
                    "model",
                    "year",
                    "description",
                    "owner"
                ])

            for row in csv_reader:
                try:
                    Car.objects.create(
                        make=row['make'],
                        model=row['model'],
                        year=row['year'],
                        description=row['description'],
                        owner_id=row['owner'],
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f'Ошибка при сохранении пользователя: {e}')
                    )

    def import_comments(self, csv_file_path):
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(
                csv_file, delimiter=',',
                fieldnames=[
                    "content",
                    "created_at",
                    "car",
                    "author"
                ])

            for row in csv_reader:
                try:
                    Comment.objects.create(
                        content=row['content'],
                        created_at=row['created_at'],
                        car_id=row['car'],
                        author_id=row['author'],
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f'Ошибка при сохранении пользователя: {e}')
                    )
