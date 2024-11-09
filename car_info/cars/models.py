from django.contrib.auth import get_user_model
from django.db import models

from .validators import validate_year

User = get_user_model()


class Car(models.Model):
    """Модель для автомобиля."""

    make = models.CharField("Марка автомобиля", max_length=50)
    model = models.CharField("Модель автомобиля", max_length=50)
    year = models.PositiveIntegerField("Год выпуска",
                                       validators=[validate_year])
    description = models.TextField("Описание автомобиля")
    created_at = models.DateTimeField("Дата и время создания записи",
                                      auto_now_add=True)
    updated_at = models.DateTimeField("Дата и время обновления записи",
                                      auto_now=True)
    owner = models.ForeignKey(User, verbose_name="Владелец",
                              on_delete=models.CASCADE)

    def __str__(self):
        return (f'Автомобиль {self.make} {self.model}')

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['-updated_at', ]


class Comment(models.Model):
    """Модель для комментария."""

    content = models.CharField("Текст комментария", max_length=100)
    created_at = models.DateTimeField("Дата и время создания",
                                      auto_now_add=True)
    car = models.ForeignKey(Car, models.CASCADE, verbose_name="Автомобиль",
                            related_name='comments')
    author = models.ForeignKey(User, models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return (f'Комментарий пользователя {self.author.username}')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at', ]
