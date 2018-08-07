
# from api.serializers import CourseSerializers
from django.conf.urls import url
from api.views import course
from api import views

urlpatterns = [
    # c
    url(r"courses/$", course.CoursesView.as_view()),
    # e
    url(r"course/(?P<pk>\d+)/$", course.CourseView.as_view()),
    # f
    url(r"course/(?P<pk>\d+)/question/$", course.CourseQuestionView.as_view()),
    # g
    url(r"course/(?P<pk>\d+)/outline/$", course.CourseOutlineView.as_view()),
    # h
    url(r"course/(?P<pk>\d+)/chapter/$", course.CourseChapterView.as_view()),
    # a
    url(r"degree_course/$", course.DegreeCourseView.as_view()),
    # d
    url(r"degree_course/(?P<pk>\d+)/mokuai/$", course.DegreeoneView.as_view()),
    # b
    url(r"degree_scholar/$", course.DegreeScholarView.as_view()),
    url(r"courses/(?P<pk>\d+)/$", course.CoursesDetailView.as_view()),
]

# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'course',views.CourseViewSet)
# urlpatterns += router.urls