import redis
import json

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,FormParser
from django.conf import settings

from api import models
from api.utils.response import BaseResponse

CONN = redis.Redis(host="192.168.11.175",port=6379) # 全局变量 大写  PEP8规范
USER_ID = 1
class ShoppingCarView(ViewSetMixin,APIView):
    # parser_classes = [JSONParser,]  # 可放入配置文件中 settings
    # JSONParser 解析器
        # 可以自动去请求体中获取请求数据，然后进行字节转字符串，json.loads反序列化。
    # 一般统一数据格式，只启用一种数据传输格式
    # parser_classes = [JSONParser,FormParser,]
    def list(self,request,*args,**kwargs):
        response = BaseResponse()
        key = settings.SHOPPING_CAR %(USER_ID,'*',)
        user_key_list = CONN.keys(key)   # 获取的是一个列表
        shopping_car_course_list = []
        for key in user_key_list:
            temp = {
                # 传过来的皆是字节类型的数据，所以需要解码
                "id":CONN.hget(key,"id").decode("utf-8"),
                "name":CONN.hget(key,"name").decode("utf-8"),
                "default_price_id":CONN.hget(key,"default_price_id").decode("utf-8"),
                "price_policy_list":json.loads(CONN.hget(key,"price_policy_list").decode("utf-8")),
            }
            # 将获得的商品数据(字典形式)，加入到列表中
            shopping_car_course_list.append(temp)
        response.data = shopping_car_course_list
        return Response(response.dict)

    def create(self,request,*args,**kwargs):
        response = BaseResponse()
        # 获取发送来的课程id 与 价格策略id

        # 购物车限制数量
        key = settings.SHOPPING_CAR %(USER_ID,"*")
        key_list = CONN.keys(key)
        if key_list and len(key_list) >= 1000:
            response.code = 500
            response.error = "购物车已满，请先结算"
            return Response(response.dict)



        course_id = request.data.get("course_id")
        policy_id = request.data.get("policy_id")

        # 查询是否具有这样的课程
        course_obj = models.Course.objects.filter(id=course_id).first()
        if not course_obj:
            response.code = 500
            response.error = "不存在课程"
        # 将此课程的全部价格策略获取
        policy_queryset = course_obj.price_policy.all()
        # 创建一个新字典，将每一个价格策略以自己的id为键添加到此字典中
        # 为了方便后面查询价格策略，
        policy_dict = {}
        for item in policy_queryset:
            temp = {
                "id": item.id,
                "price":item.price,
                "valid_period":item.valid_period,
                "valid_period_display":item.get_valid_period_display()
            }
            # 循环出每一个价格策略，使其生成字典的形式，
            policy_dict[item.id] = temp
            # 以价格策略的id 为键，生成的字典为值。添加到新字典中。
        if policy_id not in policy_dict:
            response.code = 500
            response.error = "不合法的价格策略"
            return Response(response.dict)

        #  以上两种条件满足时，将加入购物车
        '''
        redis 是一个大字典的形式：
        且只能套一个字典，无法套更多的字典:
        CONN.hget(key,id,"课程")，
        CONN.hget(key,name,"课程名称")，
        CONN.hget(key,default_price_id,"默认价格id")，
        CONN.hget(key,price_policy_list,"全部价格策略")，
        {
            shopping_car_用户id_课程id:{
                "id": 课程id,
                "name":课程名称,
                "default_price_id":默认价格id,
                "price_policy_list":全部价格策略,
            }
        }
        '''
        key = settings.SHOPPING_CAR %(USER_ID,course_id)
        CONN.hset(key,"id",course_id)
        CONN.hset(key,"name",course_obj.name)
        CONN.hset(key,"default_price_id",policy_id)
        CONN.hset(key,"price_policy_list",json.dumps(policy_dict))
        response.data = "添加成功"
        # print(CONN.hgetall(key))
        return Response(response.dict)

    def destroy(self,request,*args,**kwargs):
        response = BaseResponse()
        try:
            # 获取到用户传来的课程id
            course_id = request.data.get("course_id")
            # print(course_id)
            # 通过拼接购物车里的键
            key = settings.SHOPPING_CAR %(USER_ID,course_id)
            # delete(key) 方法 ，可以直接删除键为key的字典
            CONN.delete(key)
            response.data = "删除成功"
        except Exception as e:
            response.code = 500
            response.error = "删除失败"
        return Response(response.dict)

    def update(self,request,*args,**kwargs):
        '''
        修改，只修改默认价格id即可
        1，需确认id是否存在
        2，只需去redis校验就可以了
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        # 获取前端发来的course_id,价格策略id

        response = BaseResponse()
        try:
            # 获取课程及价格策略id
            course_id = request.data.get("course_id")
            policy_id = str(request.data.get("policy_id"))

            key = settings.SHOPPING_CAR %(USER_ID,course_id)

            # 判断课程是否存在，即 键存在不存在购物车中
            if not CONN.exists(key):
                response.code = 500
                response.error = "不存在的课程"
                return Response(response.dict)

            # 从redis 中获取该物品的所有价格策略
            price_policy_dict = json.loads(CONN.hget(key,"price_policy_list").decode('utf-8'))

            # 判断传来的价格策略id是否存在于所有的价格策略中
            if policy_id not in price_policy_dict:
                response.code = 500
                response.error = "不存在的价格策略"
                return Response(response.dict)

            # 若是存在则直接修改redis中的默认价格id.
            CONN.hset(key,"default_price_id",policy_id)
            response.data = "修改成功"
        except Exception as e:
            response.code = 500
            response.error = "修改失败"
        return Response(response.dict)
