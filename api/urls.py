from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet, UserCreate, \
                AdminViewSet, StudentViewSet, \
                TeacherViewSet, ParentViewSet, \
                StageViewSet, CategoryViewSet, \
                SubjectViewSet, QuestionnairViewSet, \
                QanswerViewSet

from .apiviews import LoginView, UserCreate

from . import views 

# Define routes
router = DefaultRouter()
router.register('users',         UserViewSet)
router.register('admins',        AdminViewSet)
router.register('students',      StudentViewSet)
router.register('teachers',      TeacherViewSet)
router.register('parents',       ParentViewSet)
router.register('stages',        StageViewSet)
router.register('categorys',     CategoryViewSet)
router.register('subjects',      SubjectViewSet)
router.register('questionnairs', QuestionnairViewSet)
router.register('qanswers',      QanswerViewSet)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path('users/create/', UserCreate.as_view())
]

urlpatterns += router.urls