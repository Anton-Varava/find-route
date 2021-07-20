from django.urls import path
from . import views


urlpatterns = [
    path('list', views.TrainListView.as_view(), name='list-train'),
    path('add', views.TrainCreateView.as_view(), name='add-train'),
    path('<int:pk>/delete', views.TrainDeleteView.as_view(), name='delete-train'),
    path('<int:pk>/edit', views.TrainUpdateView.as_view(), name='update-train')
]