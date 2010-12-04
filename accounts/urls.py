from django.conf.urls.defaults import *

urlpatterns = patterns('accounts.views',
    url(r'^login/', 'login', name='login'),
    url(r'^logout/', 'logout', name='logout'),
    url(r'^new_user/', 'new_user', name='new_user'),
)
