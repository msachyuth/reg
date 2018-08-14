from django.conf.urls import url, include
from django.contrib import admin
from regapp.views import RegisterUserView

urlpatterns = [
    url(r'^reg', view=RegisterUserView.as_view(), name='register')
]
