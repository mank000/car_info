from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path, reverse_lazy
from django.views.generic.edit import CreateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="cars_info",
        default_version='v1',
        description="Документация для cars_info",
        contact=openapi.Contact(email="ARTEM"),
        license=openapi.License(name="Hi"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

handler404 = 'cars.views.custom_404_view'
handler500 = 'cars.views.custom_500_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("django.contrib.auth.urls")),
    path(
        'auth/signup/',
        CreateView.as_view(
            template_name='registration/signup.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('login'),
        ),
        name='signup',
    ),
    path('', include('cars.urls', namespace='cars')),
    path('api/', include('api.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/auth/', include('djoser.urls')),
    path('swagger<format>/',
         schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
]
