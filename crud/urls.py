from . import views
from django.urls import re_path as url,path

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^create1$', views.create1, name='create1'),
    url(r'^create2$', views.create2, name='create2'),
    url(r'^create4$', views.create4, name='create4'),
    url(r'^create5$', views.create5, name='create5'),
    url(r'^create7$', views.create7, name='create7'),


    url(r'^list$', views.list, name='list'),
    url(r'^list1$', views.list1, name='list1'),
    url(r'^list2$', views.list2, name='list2'),
    url(r'^list4$', views.list4, name='list4'),
    url(r'^list5$', views.list5, name='list5'),
    url(r'^list6$', views.list6, name='list6'),
    url(r'^list7$', views.list7, name='list7'),
    url(r'^list8$', views.list8, name='list8'),

    url(r'^fileupload$', views.fileupload, name='fileupload'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^edit1/(?P<id>\d+)$', views.edit1, name='edit1'),
    url(r'^show1/(?P<id>\d+)$', views.show1, name='show1'),
    
    url(r'^edit1/update1/(?P<id>\d+)$', views.update1, name='update1'),
    url(r'^delete1/(?P<id>\d+)$', views.delete1, name='delete1'),
    url(r'^edit2/(?P<id>\d+)$', views.edit2, name='edit2'),
    url(r'^edit2/update2/(?P<id>\d+)$', views.update2, name='update2'),
    url(r'^delete2/(?P<id>\d+)$', views.delete2, name='delete2'),
    url(r'^edit4/(?P<id>\d+)$', views.edit4, name='edit4'),

    url(r'^edit4/update4/(?P<id>\d+)$', views.update4, name='update4'),
    url(r'^delete4/(?P<id>\d+)$', views.delete4, name='delete4'),
    url(r'^edit5/(?P<id>\d+)$', views.edit5, name='edit5'),
    url(r'^edit5/update5/(?P<id>\d+)$', views.update5, name='update5'),
    url(r'^delete5/(?P<id>\d+)$', views.delete5, name='delete5'),

    url(r'^edit7/(?P<id>\d+)$', views.edit7, name='edit7'),
    url(r'^edit7/update7/(?P<id>\d+)$', views.update7, name='update7'),
    url(r'^delete7/(?P<id>\d+)$', views.delete7, name='delete7'),

    url(r'^ajax/$', views.ajax, name='ajax'),
    url(r'^ajax/ajax$', views.ajax, name='ajaxpost'),
    url(r'^ajax/delete$', views.ajax_delete, name='ajax_delete'),
    url(r'^ajax/getajax$', views.getajax, name='getajax'),
    url(r'^register/$', views.register,name='register'),
    url(r'^register/success/$',views.register_success,name='register_success'),
    url(r'^users/$',views.users,name='users'),
    url(r'^users/delete/(?P<id>\d+)$', views.user_delete, name='user_delete'),
    url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
    url(r'^change_password$', views.changePassword, name='changePassword'),
    url(r'^file/delete$', views.changePassword, name='changePassword'),
    url(r'^file/delete/(?P<id>\d+)$', views.deleteFiles, name='deleteFiles'),
]