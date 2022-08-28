from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register('plan', views.TodoView)
router.register('solution', views.SolutionView)
urlpatterns = [
    path('', include(router.urls)),
]
