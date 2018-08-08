from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.versioning import URLPathVersioning
from rest_framework.response import Response
from api.serializers import course
from api import models
from api.utils.response import BaseResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ViewSetMixin
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,ListModelMixin
from rest_framework.viewsets import GenericViewSet

class CoursesView(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        result = BaseResponse()
        try:
            course_list = models.Course.objects.all()
            ser_obj = course.CourseSerializers(course_list,many=True)
            result.data = ser_obj.data
        except Exception as e:
            result.code = 500
            result.error = "无法获取数据"
        return Response(result.dict)

    def create(self,request,*args,**kwargs):
        print(request.body)

        return Response({"code":1})
    def retrieve(self,request,pk,*args,**kwargs):
        result = BaseResponse()
        try:
            course_obj = models.Course.objects.get(id=pk)
            ser_obj = course.CourseSerializers(course_obj)
            result.data = ser_obj.data
        except Exception as e:
            result.code = 500
            result.error = "无法获取数据"
        return Response(result.dict)


class AuthView(ViewSetMixin,APIView):

    def login(self,request,*args,**kwargs):
        print("用户法来POST请求了",request.body)
        return Response({"code":1111})
