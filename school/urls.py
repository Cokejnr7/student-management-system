from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet,FacultyViewSet,ProgrammeViewSet,CourseViewSet

router = DefaultRouter()

router.register('departments',DepartmentViewSet)
router.register('facultys',FacultyViewSet)
router.register('programmes', ProgrammeViewSet)
router.register('Courses',CourseViewSet)

urlpatterns = router.urls
