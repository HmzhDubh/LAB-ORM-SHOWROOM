from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [

    path('', views.home_view, name='home_view'),
    path('search/', views.search_view, name="search_view"),
    path('test_drive_request/', views.test_drive_view, name='test_drive_view'),

]
