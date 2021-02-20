from django.urls import path

from . import  views

app_name = 'greet'
urlpatterns = [
    path('', views.index, name = 'index'),
    # ex: http://192.168.0.153:8888/greet/name/
    # 注意 url中有greet（应用名）
    path('<str:name>/', views.greet, name = 'greet')
]