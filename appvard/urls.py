"""
URL configuration for appvard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from IDE.views import ConnectToRemoteDB
from vard.views import *
from django.conf.urls.static import static
from django.conf import settings
from uploadfiles.views import FileUploadView, UploadViaLink

router = routers.DefaultRouter()
router.register(r'users', MyUserViewSet)
router.register(r'files', FileViewSet)
router.register(r'access', AccessViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'dashboard', DashboardViewSet)
router.register(r'chart', ChartViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'readcomment', ReadCommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/vard-auth/', include('rest_framework.urls')), #+login +logout - вход/Выход (POST)
    path('api/v1/auth/', include('djoser.urls')), # + /users/ - регистрация (POST)
    re_path(r'^auth/', include('djoser.urls.authtoken')), # АВТОРИЗАЦИЯ ПО ТОКЕНУ (POST)
    path('api/v1/', include(router.urls)),  # CRUD для моделей (GET, POST, PUT, DELETE)
    path('api/v1/connect-to-external-db/', ConnectToRemoteDB.as_view(), name='connect_to_external_db'), # подключение к БД
    path('api/v1/execute-sql-query/', ConnectToRemoteDB.as_view(), name='execute_sql_query'), # выполнение sql
    path('api/v1/upload-file/', FileUploadView.as_view(), name='upload-file'),
    path('api/v1/upload-file/link', UploadViaLink.as_view(), name='link-file'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)