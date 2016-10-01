from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^error$', views.error, name='error'),
    url(r'^sign_in$', views.sign_in, name='sign_in'),
    url(r'^add_book$', views.add_book, name='add_book'),
    url(r'^add_clothes$', views.add_clothes, name='add_clothes'),
    url(r'^add_medicine$', views.add_medicine, name='add_medicine'),
    url(r'^add_tech$', views.add_tech, name='add_tech'),
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout_user, name='logout'),
]
