from datetime import date

from django.core.exceptions import ValidationError


def validate_year(year):
    """Проверка на то, чтобы указанный год был меньше текущего."""

    year_now = date.today().year
    if year > year_now:
        raise ValidationError("Год выпуска не может быть больше текущего.")
