"""questionbox_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from questionbox import views as api_views



router = DefaultRouter(trailing_slash=False)
router.register("questions", api_views.QuestionViewSet, basename="questions")

urlpatterns = [
    path("api/", include(router.urls)),
    path('admin/', admin.site.urls),
    #rest framework
    path('api-auth/', include('rest_framework.urls')),
    #djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    # api paths

    # answer paths
    path("api/questions/<int:questions_pk>/answers",
                api_views.AnswerViewSet.as_view({
                    'get': 'list',
                    'post': 'create',
                }),
                name="api_question_answers"
    ),
    path("api/questions/<int:questions_pk>/answers/<int:pk>",
                api_views.AnswerViewSet.as_view({
                    'get': 'retrieve',
                    'put': 'update',
                    'patch': 'partial_update',
                    'delete': 'destroy',
                }),
                name="api_question_answers_detail"
    ),

    # search path
    path('api/questions/', api_views.QuestionSearchView.as_view())
]