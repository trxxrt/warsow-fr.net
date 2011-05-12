from django.conf.urls.defaults import *

urlpatterns = patterns('users.views',
    (r'^register/', 'register'),
)

