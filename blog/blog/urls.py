from django.contrib import admin
from django.urls import include, path 
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Blog API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')), 
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('schema/', schema_view),
]