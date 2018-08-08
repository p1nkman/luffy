from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.versioning import URLPathVersioning
from rest_framework.response import Response
from api.serializers import course
from api import models
from api.utils.response import BaseResponse

class CoursesView(APIView):

    def get(self, request, *args, **kwargs):

        result = BaseResponse()
        # result.dict = {"code":1000,"data":None,"error":None}
        # print(result.dict)
        print(request.version)   # 打印请求发送来的数据中获取的version
        try:
            course_list = models.Course.objects.filter(degree_course__isnull=True)
            print(course_list)
            ser_obj = course.CourseSerializers(course_list,many=True)
            result.data = ser_obj.data
        except Exception as e:
            result.code = 500
            result.error = "获取数据失败"
        return Response(result.dict)


class CoursesDetailView(APIView):

    def get(self,request,pk,*args,**kwargs):
        result = BaseResponse()
        try:
            course_obj = models.Course.objects.get(id=pk)
            ser_obj = course.CourseSerializers(course_obj)
            result.data = ser_obj.data
        except Exception as e:
            result.code = 500
            result.error = "获取数据失败"
        return Response(result.dict)


class DegreeCourseView(APIView):

    def get(self,request,*args,**kwargs):
        result = BaseResponse()
        try:
            degree_list = models.DegreeCourse.objects.all()
            ser_obj = course.DegreeSerializers(degree_list,many=True)
            result.data = ser_obj.data
        except Exception as e:
            result.code = 500
            result.error = "获取数据失败"
            print(result.dict)
        return Response(result.dict)


class DegreeScholarView(APIView):

    def get(self,request,*args,**kwargs):
        result = BaseResponse()
        # try:
        degree_list = models.DegreeCourse.objects.all()
        ser_obj = course.DegreeScholarSerializers(degree_list,many=True)
        result.data = ser_obj.data
    # except Exception as e:
        result.code = 500
        result.error = "无法获取数据"
        return Response(result.dict)


# d
class DegreeoneView(APIView):
    def get(self,request,pk,*args,**kwargs):
        result = BaseResponse()
        course_list = models.DegreeCourse.objects.get(id=pk)
        ser_obj = course.DegreeMokuaiSerializers(course_list)
        result.data = ser_obj.data
        return Response(result.dict)


# e  获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
class CourseView(APIView):
    def get(self,request,pk,*args,**kwargs):
        result = BaseResponse()
        course_obj = models.Course.objects.get(id=pk)
        ser_obj = course.Course_Serializers(course_obj)
        result.data = ser_obj.data
        return Response(result.dict)


# f.获取id = 1的专题课，并打印该课程相关的所有常见问题
class CourseQuestionView(APIView):
    def get(self,request,pk,*args,**kwargs):
        result = BaseResponse()
        course_obj = models.Course.objects.get(id=pk)
        ser_obj = course.CourseQuestionSerializer(course_obj)
        result.data = ser_obj.data
        return Response(result.dict)


# g.获取id = 1的专题课，并打印该课程相关的课程大纲
class CourseOutlineView(APIView):
    def get(self,request,pk,*args,**kwargs):
        result = BaseResponse()
        course_obj = models.Course.objects.get(id=pk)
        ser_obj = course.CourseOutlineSerializers(course_obj)
        result.data = ser_obj.data
        return Response(result.dict)


# h.获取id = 1的专题课，并打印该课程相关的所有章节
class CourseChapterView(APIView):
    def get(self,request,pk,*args,**kwargs):
        result = BaseResponse()
        course_obj = models.Course.objects.get(id=pk)
        ser_obj = course.CourseChapterSerializers(course_obj)
        result.data = ser_obj.data
        return Response(result.dict)

