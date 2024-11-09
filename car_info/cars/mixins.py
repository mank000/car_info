from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Car


class CarModelMixin:
    """Миксин с моделью."""

    model = Car


class CarDispatchMixin:
    """Миксин с проверкой на создателя."""

    success_url = reverse_lazy('cars:index')

    def dispatch(self, request, *args, **kwargs):
        instance = get_object_or_404(Car, pk=kwargs['pk'])
        if instance.owner != self.request.user:
            return redirect('detail', pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)


class CarFieldsMixin:
    """Миксин с полями для создания/изменения."""

    success_url = reverse_lazy('cars:index')
    fields = ['make', 'model', 'year', 'description']
