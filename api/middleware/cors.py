
#  此py文件只为了在中间件中增加跨域的响应值

from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class CorsMiddleware(MiddlewareMixin):

    def process_response(self,request,response):
        response["Access-Control-Allow-Origin"] = "http://localhost:8080"
        # 将你想跨域的地址（url）加到 后面，如上。
        if request.method == "OPTIONS":
            response["Access-Control-Allow-Methods"] = "PUT,DELETE"
            # 请求方式的放行(简言之，就是可以允许以上请求方式的跨域行为)
            response["Access-Control-Allow-Headers"] = "Content-Type"

            # 在 settings 设置后可写成如下等同于上面的：
            # response["Access-Control-Allow-Methods"] = settings.CORS_METHODS
            # response["Access-Control-Allow-Headers"] = settings.CORS_HEADERS
        return response