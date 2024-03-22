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
from IDE.views import SQLQueryView, DatabaseConnectionView
from vard.views import *

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
    path('api/v1/connect/',DatabaseConnectionView.as_view()), # Подключение к БД (POST)
    path('api/v1/sql/', SQLQueryView.as_view())  # ОТПРАВКА SQL ЗАПРОСА (POST)

]
