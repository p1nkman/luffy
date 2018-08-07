from django.shortcuts import render,HttpResponse
from api import models
# Create your views here.

def index(request):
    # a.查看所有学位课并打印学位课名称以及授课老师
    # obj = models.DegreeCourse.objects.all().values("name","teachers__name")
    # print(obj)

    # b.查看所有学位课并打印学位课名称以及学位课的奖学金
    # obj = models.DegreeCourse.objects.all().values("name","scholarship__value")
    # print(obj)

    # c.展示所有的专题课
    # course_obj = models.Course.objects.filter(degree_course__isnull=True)
    # print(course_obj)

    # d.查看id = 1 的学位课对应的所有模块名称
    # degree_obj = models.DegreeCourse.objects.filter(id = 1).first()
    # print(degree_obj)

    # e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    obj = models.Course.objects.filter(id=1).first()
    print(obj.name,obj.get_level_display(),obj.coursedetail.why_study,obj.coursedetail.what_to_study_brief,obj.coursedetail.recommend_courses.all())

    # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
    # question_list = models.Course.objects.filter(id=1).first()
    # query_set = question_list.asked_question.all()
    # for i in query_set:
    #     print(i.question)

    # g.获取id = 1的专题课，并打印该课程相关的课程大纲
    # courseoutline_list = models.CourseOutline.objects.filter(course_detail__course__pk=1).values("title")
    # print(courseoutline_list)

    # h.获取id = 1的专题课，并打印该课程相关的所有章节
    # coursechapter_list = models.CourseChapter.objects.filter(course__pk=1).values("name")
    # print(coursechapter_list)

    # i.获取id = 1的专题课，并打印该课程相关的所有课时
    # query_set = models.CourseSection.objects.all().values("chapter__name","name")
    # print(query_set)


    # i.获取id = 1的专题课，并打印该课程相关的所有的价格策略
    # query_obj = models.Course.objects.filter(id=1).first()
    # print(query_obj.price_policy.all())
    return HttpResponse("index")


