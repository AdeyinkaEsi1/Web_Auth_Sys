from django.urls import path
from .views import Text
from . import views


urlpatterns = [
    path('', views.Text, name='home'),
    # path('Thanks/', views.Thanks, name='Thanks')
]

