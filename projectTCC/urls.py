from django.contrib import admin
from django.urls import path, include
from aluno.views import HomeTemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    
]+ static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
