from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^error$', views.error, name='error'),
    url(r'^detail$', views.detail, name='detail'),
    url(r'^faq$', views.faq, name='faq'),
    url(r'^sign_in$', views.sign_in, name='sign_in'),
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout_user, name='logout'),
]
