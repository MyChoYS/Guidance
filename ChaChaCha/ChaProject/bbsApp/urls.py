from django.urls import path
from . import views
urlpatterns=[
    path('review/', views.review_academy, name='review'),
    path('review_academy/', views.review_academy, name='review_academy'),
    path('review_testsite/', views.review_testsite, name='review_testsite'),
    path('delete_academy/', views.delete_academy, name='delete_academy'),
    path('delete_testsite/', views.delete_testsite, name='delete_testsite'),
]