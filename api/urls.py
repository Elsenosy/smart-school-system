from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apiviews import UserViewSet, UserCreate, LoginView, AdminViewSet, StudentViewSet, TeacherViewSet, ParentViewSet
from . import views 

# Define routes
router = DefaultRouter()
router.register('users', UserViewSet)
router.register('admins', AdminViewSet)
router.register('students', StudentViewSet)
router.register('teachers', TeacherViewSet)
router.register('parents', ParentViewSet)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
]

urlpatterns += router.urls