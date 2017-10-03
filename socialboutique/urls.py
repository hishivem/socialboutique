from django.conf.urls import url, include
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/', views.SignUpView.as_view(), name="signup"),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^join-us/$', views.JoinusView.as_view(), name='join-us'),
    url(r'^your-requirements/$', views.YourrequirementsView.as_view(), name='your-requirements'),
]