from django.urls import path
from youtube_rename_app import views
urlpatterns = [
path('', views.dashboard, name='dashboard'),
path('<int:pk>/name_updater_poll', views.name_updater_poll, name='name_updater_poll'),
path('name_updater', views.name_updater, name='name_updater')


]