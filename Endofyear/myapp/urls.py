from django.conf.urls import url
from myapp import views

# template url
app_name = 'myapp'
urlpatterns =[
    url(r'^register/$',views.register,name='register'),
    url(r'^lichess/$',views.lichess,name='lichess'),
    url(r'^ls/$',views.user_login,name='loging'),
    url(r'tolgaçalım',views.tolgaçalım,name="tolgaçalım"),

]
