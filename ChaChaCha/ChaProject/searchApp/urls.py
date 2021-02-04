from django.urls import path
from . import views
urlpatterns=[
    path('services1/', views.services1, name='services1'),
    path('services2/', views.services2, name='services2'),
    path('services3/', views.services3, name='services3'),
    path('tt/', views.tt, name='tt'), # 지도 테스트. 나중에 지우기
]