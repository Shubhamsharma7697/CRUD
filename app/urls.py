
from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name='home'),
    path("home/",home,name="home"),
    path("add_stu/",add_stu,name="add_stu"),
    path("delete_stu/<int:roll>",delete_stu,name="delete_stu"),
    path("update_stu/<int:roll>",update_stu),
    path("do_update_stu/<int:roll>",do_update_stu),
]
