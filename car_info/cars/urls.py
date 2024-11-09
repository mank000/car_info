from django.urls import path

from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='detail'),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view(), name='delete'),
    path('car/<int:pk>/edit/', views.CarUpdateView.as_view(), name='edit'),
    path('car/', views.CarCreateView.as_view(), name='create'),
    path('car/<int:pk>/comment/',
         views.CommentCreateView.as_view(), name='comment'),
]
