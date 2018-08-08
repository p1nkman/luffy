
from django.conf.urls import url
from api.views import course
from api import views



urlpatterns = [
    # 如果as_view()里面要传参数的话，前提视图CBV必须继承 ViewSetMixin ,这样才能往as_view()中传入参数。
    # 键值对的形式，表明了各请求方式对应的方法，所以特定的请求方式，便可执行相应的方法。
    # 如果as_view()里写了相应的键值对，在视图CBV中必须写出相应的方法。

    url(r'courses/$',course.CoursesView.as_view({'get':'list'})),

    url(r'courses/(?P<pk>\d+)/$',course.CoursesView.as_view({'get':'retrieve'}))
]

# urlpatterns = [
#     # c
#     url(r"courses/$", course.CoursesView.as_view()),
#     # e
#     url(r"course/(?P<pk>\d+)/$", course.CourseView.as_view()),
#     # f
#     url(r"course/(?P<pk>\d+)/question/$", course.CourseQuestionView.as_view()),
#     # g
#     url(r"course/(?P<pk>\d+)/outline/$", course.CourseOutlineView.as_view()),
#     # h
#     url(r"course/(?P<pk>\d+)/chapter/$", course.CourseChapterView.as_view()),
#     # a
#     url(r"degree_course/$", course.DegreeCourseView.as_view()),
#     # d
#     url(r"degree_course/(?P<pk>\d+)/mokuai/$", course.DegreeoneView.as_view()),
#     # b
#     url(r"degree_scholar/$", course.DegreeScholarView.as_view()),
#     url(r"courses/(?P<pk>\d+)/$", course.CoursesDetailView.as_view()),
# ]

# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'course',views.CourseViewSet)
# urlpatterns += router.urls