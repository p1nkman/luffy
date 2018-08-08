# from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from api import models

class CourseSerializers(serializers.ModelSerializer):
    level = serializers.CharField(source="get_level_display")
    price_period = serializers.SerializerMethodField()
    class Meta:
        model = models.Course
        # fields = "__all__"
        fields = ["name","level","price_period"]
        # depth = 5

    def get_price_period(self,row):
        price_list = row.price_policy.all()
        return [{"period": str(i.valid_period)+"天","price":i.price } for i in price_list]



class DegreeSerializers(serializers.ModelSerializer):
    teacher_name = serializers.SerializerMethodField()
    # teacher_name = serializers.CharField(source="teachers.")
    class Meta:
        model = models.DegreeCourse
        fields = ["name","teacher_name"]

    def get_teacher_name(self,row):
        teacher_list = row.teachers.all()
        return [{"name": i.name } for i in teacher_list]


class DegreeScholarSerializers(serializers.ModelSerializer):
    # scholar = serializers.CharField(source="scholarship_set.all")
    scholar = serializers.SerializerMethodField()
    class Meta:
        model = models.DegreeCourse
        fields = ["name","scholar"]

    def get_scholar(self,row):
        scholar_list = row.scholarship_set.all()
        return [{"scholar": i.value} for i in scholar_list]

class DegreeMokuaiSerializers(serializers.ModelSerializer):
    # degree_mokuai = serializers.CharField(source="")
    # print(111)
    class Meta:
        model = models.DegreeCourse
        fields = ["name"]
        # fields = "__all__"


class Course_Serializers(serializers.ModelSerializer):
    level = serializers.CharField(source="get_level_display")
    why_study = serializers.CharField(source="coursedetail.why_study")
    what_to_study_brief = serializers.CharField(source="coursedetail.what_to_study_brief")
    recommend_courses = serializers.SerializerMethodField()
    class Meta:
        model = models.Course
        fields = ["name","level","why_study","what_to_study_brief","recommend_courses"]

    def get_recommend_courses(self,row):
        recomment_list = row.coursedetail.recommend_courses.all()
        return [{"id":item.id,"name":item.name} for item in recomment_list]


class CourseQuestionSerializer(serializers.ModelSerializer):
    # question = serializers.CharField(source="asked_question.all")
    question = serializers.SerializerMethodField()
    class Meta:
        model = models.Course

        fields = ["name","question"]

    def get_question(self,row):
        question_list = row.asked_question.all()
        return [{"question":i.question,"answer":i.answer} for i in question_list]


class CourseOutlineSerializers(serializers.ModelSerializer):
    courseoutline = serializers.SerializerMethodField()
    class Meta:
        model = models.Course
        fields = ["name","courseoutline"]
        # fields = "__all__"

    def get_courseoutline(self,row):
        outline_list = row.coursedetail.courseoutline_set.all()
        return [{"courseoutline":i.title,"content":i.content} for i in outline_list]


class CourseChapterSerializers(serializers.ModelSerializer):
    course_chapter = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ["name","course_chapter"]

    def get_course_chapter(self,row):
        course_chapter_list = row.coursechapters.all()
        return [{"chapter": i.name} for i in course_chapter_list]