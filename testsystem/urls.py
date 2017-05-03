from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^get_new_temp_test/$', views.get_new_temp_test),
    url(r'^(?P<subject_t>[\w-]+)$', views.info_subject, name = 'info_subject'),
    url(r'^(?P<subject_t>[\w-]+)/(?P<id>[0-9]+)$', views.static_test, name = 'static_test'),
    url(r'^(?P<subject_t>[\w-]+)/(?P<id>[0-9]+)$', views.static_test, name = 'static_test')

]

"""
url(r'^(?P<subject_t>[\w-]+)$', views.get_info_subject, name='get info'),
url(r'^(?P<subject_t>[\w-]+)/$', views.get_info_subject, name='get info'),
url(r'^api/tasks/$', views.tasks_list),
"""