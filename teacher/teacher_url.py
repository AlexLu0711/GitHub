from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'Alex_Django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 视图函数名称只有名称，无括号和参数
    url(r'luyang/', views.do_app),

]
