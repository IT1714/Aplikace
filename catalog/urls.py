from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.GameListView.as_view(), name='list'),
    path('detail/<str:pk>', views.GameDetailView.as_view(), name='detail')
]