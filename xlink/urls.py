from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from xlink import views
urlpatterns = [
    # ... 他のURLパターン ...
    path('accounts/', views.index, name="index"),
    path('', views.home, name="home"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)