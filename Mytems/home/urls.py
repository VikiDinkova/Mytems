from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^error$', views.error, name='error'),
    url(r'^sign-in$', views.sign_in, name='sign_in'),
    url(r'^add-book$', views.add_book, name='add_book'),
    url(r'^add-clothes$', views.add_clothes, name='add_clothes'),
    url(r'^add-medicine$', views.add_medicine, name='add_medicine'),
    url(r'^add-tech$', views.add_tech, name='add_tech'),
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout_user, name='logout'),
    url(r'^drugs$', views.drugs, name='drugs'),
    url(r'^clothes', views.clothes, name='clothes'),
    url(r'^tech', views.techaccessoaries, name='tech'),
    url(r'^add-item', views.add_item, name='add_item'),
    url(r'^books', views.books, name='books'),

]
