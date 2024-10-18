from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map_view'),  
    path('get_latest_location/', views.get_latest_location, name='get_latest_location'),
# update location path as view
    path('update_location/', views.update_location, name='update_location'),

]
