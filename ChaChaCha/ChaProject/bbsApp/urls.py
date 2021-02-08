from django.urls import path
from . import views
urlpatterns=[
    path('review/', views.review_academy, name='review'),
    path('review_academy/', views.review_academy, name='review_academy'),
    path('review_testsite/', views.review_testsite, name='review_testsite'),
    path('delete_academy/', views.delete_academy, name='delete_academy'),
    path('delete_testsite/', views.delete_testsite, name='delete_testsite'),
    path('create_academy_review/', views.create_academy_review, name='create_academy_review'),
    path('create_testsite_review/', views.create_testsite_review, name='create_testsite_review'),
    path('get_academy_town/', views.get_academy_town, name='get_academy_town'),
    path('get_academy_name/', views.get_academy_name, name='get_academy_name'),
    path('get_testsite_name/', views.get_testsite_name, name='get_testsite_name'),
]