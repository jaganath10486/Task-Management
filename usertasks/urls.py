from django.urls import path
from .views import TaskView, TaskIdView, UserView

urlpatterns = [
    path('task/', TaskView.as_view()),
    path('task/<int:pk>', TaskIdView.as_view()),
]