from django.urls import path
from . import views
# replace <your_app> with your application name.
urlpatterns = [
    path('', views.index)

    ]