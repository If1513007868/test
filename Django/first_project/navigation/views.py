from django.http import HttpResponse

from django.shortcuts import render
# 首先，构建一个字典，设定要传给模板的数据。然后，
# 调用 render() 辅助函数。这个函数的参数 是 request 对象、模板的文件名和上下文字典。
# render() 函数将把上下文字典中的数据代入模 板，生成一个完整的 HTML 页面，
# 作为 HttpResponse 对象返回，分发给 Web 浏览器
def index(request):
    # 构建一个字典，作为上下文传给模板引擎
    # 注意， boldmessage 键对应于模板中的 {{ boldmessage }}
    context_dict = {'boldmessage': "女神, 屌丝, pythoner"}  #模板中的变量
    # 返回一个渲染后的响应发给客户端
    # 为了方便，我们使用的是 render 函数的简短形式
    # 注意，第二个参数是我们想使用的模板
    return render(request,'navigation/index.html',context=context_dict)
def about(request):
    return HttpResponse("龙腾测试！！！ <a href='/navigation/'>首页</a>")
