from django.urls import path

from birds.apps import BirdsConfig
from birds.views import BirdsListView, BirdsCreateView, BirdsDetailView, \
    BirdsUpdateView, BirdsDeleteView, view_birds, ViewBirdsListView

app_name = BirdsConfig.name

urlpatterns = [
    path('', BirdsListView.as_view(), name='list'),
    path('create/', BirdsCreateView.as_view(), name='create'),
    path('view/<int:pk>/', BirdsDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BirdsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BirdsDeleteView.as_view(), name='delete'),
    path('<int:pk>/birds/', view_birds, name='birds_view'),
    path('view_birds/', ViewBirdsListView.as_view(), name='view_birds')
]