from django.urls import path
from crud.views import *

urlpatterns = [
    path('', HomeView.as_view(), name=''),
    path('home', HomeView.as_view(), name='home'),
    path('membre_create', MembreCreateView.as_view(), name='membre_create'),
    path('membre_read/<int:pk>/', MembreDetailView.as_view(), name='membre_read'),
    path('membre_update/<int:pk>/', MembreUpdateView.as_view(), name='membre_update'),
    path('membre_delete/<int:pk>/', MembreDeleteView.as_view(), name='membre_delete'),
    path('membre_list', MembreListView.as_view(), name='membre_list'),
]
