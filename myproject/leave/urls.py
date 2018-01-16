from django.conf.urls import url
from leave.views import LeaveList


urlpatterns = [
url(r'^leave/$', LeaveList.as_view()),
]