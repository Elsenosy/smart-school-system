from django.urls import path, include
from django.conf.urls import include, url
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet, UserCreate, \
                StageViewSet, CategoryViewSet, \
                SubjectViewSet, QuestionnairViewSet, \
                QanswerViewSet, MaterialViewSet, \
                ExamViewSet, ExamQuestionViewSet, \
                ExamQuestionAnswerViewSet

from django.conf.urls.static import static
from django.conf import settings
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
router.register('materials',     MaterialViewSet)
router.register('exams',         ExamViewSet)
router.register('materials',     ExamQuestionViewSet)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("users/<int:pk>/subjects/", UserSubjects.as_view(), name="student_subjects"),
    path("exams/{pk}/addQuestions", ExamViewSet.as_view({'post', 'addQuestions'}))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls