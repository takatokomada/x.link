from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from xlink import views
urlpatterns = [
    # ... 他のURLパターン ...
    path('accounts/', views.index, name="index"),
    path('', views.accounts, name="home"),
    path('account/<str:name>/', views.room, name="room"),
    path('profile_create/', views.form_create, name="profile_create"),
    path('class/create.html/', views.form_class, name="class_create"),
    path('community/<str:name>/', views.community, name="community"),
    path('community/comment/<str:name>/', views.form_comment, name="comment"),
    re_path(r'^compose/recomments/(?P<pk>[^/]+)/(?P<name>[^/]+)/$',  views.re_comment_form , name="re_comment_form"),
    path('follow_count', views.follow_count, name="follow_count"),
    path('root_selecter', views.root_selecter, name="root_selecter"),
    path('follow_counts', views.follow_counts, name="follow_counts"),
    path('root_count', views.root_count, name="root_count"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)