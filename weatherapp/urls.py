from django.urls import path
from . import views
from .views import FeedbackView
urlpatterns = [
    path('home', views.index, name='home'),
    path('forecast', views.get_forecast, name='forecast'),
    path('airquality', views.get_info_of_airquality, name='airquality'),
    path('feedback', FeedbackView.as_view(), name='feedback'),
    path('flycond', views.flying_conditions, name='flycond'),
    path('forecast/<int:num_day>/', views.get_hour_forecast, name='hour')
]