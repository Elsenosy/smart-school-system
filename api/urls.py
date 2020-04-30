from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet, UserCreate, \
                StageViewSet, CategoryViewSet, \
                SubjectViewSet, QuestionnairViewSet, \
                QanswerViewSet

from .apiviews import LoginView, UserSubjects

from . import views 

# Define routes
router = DefaultRouter()
router.register('users',         UserViewSet)
router.register('stages',        StageViewSet)
router.register('categorys',     CategoryViewSet)
router.register('subjects',      SubjectViewSet)
router.register('questionnairs', QuestionnairViewSet)
router.register('qanswers',      QanswerViewSet)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("users/<int:pk>/subjects/", UserSubjects.as_view(), name="student_subjects"),
]

urlpatterns += router.urls