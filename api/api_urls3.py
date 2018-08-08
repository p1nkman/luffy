
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
