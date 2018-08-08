from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.versioning import URLPathVersioning
from rest_framework.response import Response
from api.serializers import course
from api import models
from api.utils.response import BaseResponse
from rest_framework.pagination import PageNumberPagination


class CoursesView(APIView):

    def get(self,request,*args,**kwargs):
        result = BaseResponse()
        try:
            queryset = models.Course.objects.all()
            # 分页
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset,request,self)

            # 分页之后的结果执行序列化
            # 分页之后必须在序列化类中加上:instance=course_list
            ser = course.CourseSerializers(instance=course_list,many=True)
            # ser_obj = course.CourseSerializers(queryset,many=True)

            result.data = ser.data
            # result.data = ser_obj.data
        except Exception as e:
            result.code = 500
            result.error = "无法获取数据"
        return Response(result.dict)


class CourseDetailView(APIView):
    def get(self,request,pk,*args,**kwargs):
        result = BaseResponse()
        try:
            course_obj = models.Course.objects.get(id=pk)
            ser_obj = course.CourseSerializers(instance=course_obj)
            result.data = ser_obj.data
        except Exception as e:
            result.code = 500
            result.error = "无法获取数据"

        return Response(result.dict)