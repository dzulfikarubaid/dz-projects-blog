
from django.contrib import admin
from django.urls import path, include

#ckeditor
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dz_pro.urls')),
    path('auth/', include('auth_users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
