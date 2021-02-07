from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    TeachersViewSet,
    StudentViewSet,
    StudentWithTeacherListAPIView
)

router = DefaultRouter()
router.register(r'teachers', TeachersViewSet, basename='teacher')
router.register(r'student', StudentViewSet, basename='student')


urlpatterns = [
    path('^teacher/by/(?P<pk>\w+)/$', StudentWithTeacherListAPIView.as_view(), name="student_teacher"),
]

urlpatterns += router.urls