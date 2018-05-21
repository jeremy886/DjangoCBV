from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [
    path("hello", views.HelloView.as_view()),
    path("", views.HomeView.as_view()),
    path('groups', views.StudyGroupListView.as_view()),
    path("<int:pk>/", views.StudyGroupDetailView.as_view(), name="detail"),
    path("groups/create/", views.StudyGroupCreateView.as_view(), name="create"),
]