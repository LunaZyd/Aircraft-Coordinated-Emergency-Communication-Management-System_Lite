from corsheaders.middleware import CorsMiddleware
from corsheaders.signals import check_request_enabled

class CustomCorsMiddleware(CorsMiddleware):
    def process_response(self, request, response):
        # 设置允许所有 IP 访问
        response["Access-Control-Allow-Origin"] = "*"
        return super().process_response(request, response)

# 注册信号，允许所有请求
check_request_enabled.connect(lambda sender, request, **kwargs: True)
