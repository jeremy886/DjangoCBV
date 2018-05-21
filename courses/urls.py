from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [
    path("hello", views.HelloView.as_view()),
    path("", views.HomeView.as_view()),
    path('groups', views.StudyGroupListView.as_view(), name='list'),
    path("groups/<int:pk>/", views.StudyGroupDetailView.as_view(), name="detail"),
    path("groups/create/", views.StudyGroupCreateView.as_view(), name="create"),
    path("groups/update/<int:pk>/", views.StudyGroupUpdateView.as_view(), name="update"),
]