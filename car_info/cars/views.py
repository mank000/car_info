from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from . import mixins
from .models import Car, Comment


def custom_404_view(request, exception):
    """Кастомная страница 404 ответа."""

    return HttpResponseNotFound(render(request, 'pages/404.html'))


def custom_500_view(request):
    """Кастомная страница 500 ответа."""

    return HttpResponseServerError(render(request, 'pages/500.html'))


class IndexView(mixins.CarModelMixin,
                ListView):
    """View главной страницы."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = Car.objects.all()
        return context


class CarUpdateView(mixins.CarDispatchMixin,
                    mixins.CarFieldsMixin,
                    mixins.CarModelMixin,
                    LoginRequiredMixin,
                    UpdateView):
    """View обновления данных об автомобиле."""

    template_name = 'edit.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.updated_at = self.request.user
        self.object.save()
        return super().form_valid(form)


class CarDeleteView(mixins.CarDispatchMixin,
                    mixins.CarModelMixin,
                    LoginRequiredMixin,
                    DeleteView):
    """View удаления автомобиля из базы."""

    template_name = 'delete.html'


class CarDetailView(mixins.CarModelMixin,
                    DetailView):
    """View получения детальной информации об автомобиле."""

    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(car=self.kwargs['pk'])
        return context


class CarCreateView(mixins.CarModelMixin,
                    mixins.CarFieldsMixin,
                    LoginRequiredMixin,
                    CreateView):
    """View создания объекта автомобиля."""

    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    """View создания комментария."""

    model = Comment
    template_name = 'comment.html'
    fields = ['content']

    def get_success_url(self) -> str:
        return reverse('cars:detail',
                       kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.car = Car.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def dispatch(self, request, **kwargs):
        self.car = get_object_or_404(Car, id=kwargs['pk'])
        return super().dispatch(request, **kwargs)
