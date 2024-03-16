from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from xlink import views
urlpatterns = [
    # ... 他のURLパターン ...
    path('accounts/', views.index, name="index"),
    path('', views.accounts, name="home"),
    path('account/<str:name>/', views.room, name="room"),
    path('profile_create/', views.form_create, name="profile_create"),
    path('class/create.html/', views.form_class, name="class_create"),
    path('community/<str:name>/', views.community, name="community"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)