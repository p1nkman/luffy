from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.versioning import URLPathVersioning
from rest_framework.response import Response
from api.serializers import course
from api import models
from api.utils.response import BaseResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ViewSetMixin

# 继承ViewSetMixin
class CoursesView(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        result = BaseResponse()
        try:
            # 从数据库中获取数据
            queryset = models.Course.objects.all()
            ser_obj = course.CourseSerializers(queryset,many=True)

            result.data = ser_obj.data
        except Exception as e:
            result.code = 500
            result.error = "无法获取数据"
        return Response(result.dict)

    def create(self,request,*args,**kwargs):
        '''
        post方式，增加
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
    def retrieve(self,request,pk,*args,**kwargs):
        '''
        详细显示
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        '''
        result = BaseResponse()
        try:
            course_obj = models.Course.objects.get(id=pk)
            ser_obj = course.CourseSerializers(instance=course_obj)
            # print(ser_obj)
            result.data = ser_obj.data
            # print(result.data)
        except Exception as e:
            result.code = 500
            result.error = "无法获取数据"
        return Response(result.dict)

    def update(self,pk,*args,**kwargs):
        '''
        put,更改
        :param pk:
        :param args:
        :param kwargs:
        :return:
        '''

    def destroy(self,pk,*args,**kwargs):
        '''
        delete ,删除
        :param pk:
        :param args:
        :param kwargs:
        :return:
        '''
