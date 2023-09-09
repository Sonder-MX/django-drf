from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class CustomResult(dict):
    """自定义结果字典"""

    def __init__(self, data=None, code=0, msg="success", **kwargs):
        """初始化方法"""
        super().__init__(**kwargs)
        self["data"] = data
        self["code"] = code
        self["msg"] = msg

    @staticmethod
    def success(data=None, msg="success"):
        """成功结果"""
        return CustomResult(data=data, msg=msg)

    @staticmethod
    def error(msg="ERROR"):
        """失败结果"""
        return CustomResult(code=1, msg=msg)


class CustomJSONRenderer(JSONRenderer):
    """自定义 JSON 渲染器"""

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """重写 render 方法"""
        # 判断是否有错误
        if renderer_context:
            response = renderer_context["response"]
            if not response.exception:
                # 没有错误，正常返回
                return super().render(CustomResult.success(data))
            else:
                # 有错误，返回自定义结果
                first_error = list(response.data.values())[0]
                if isinstance(first_error, list):
                    first_error = first_error[0]
                return super().render(CustomResult.error(first_error))
        else:
            # 有错误，返回自定义结果
            return super().render(CustomResult.error(msg="服务器内部错误"))
