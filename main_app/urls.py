from  django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about , name='about'),
    path('arts/', views.arts_index , name='index'),
    path('arts/<int:art_id>/', views.arts_detail, name='detail'),
    path('arts/create/', views.ArtCreate.as_view(), name='arts_create'),
    path('arts/<int:pk>/update/', views.ArtUpdate.as_view(), name='arts_update'),
    path('arts/<int:pk>/delete/', views.ArtDelete.as_view(), name='arts_delete'),
    path('arts/<int:art_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('arts/<int:art_id>/assoc_location/<int:location_id>/', views.assoc_location, name='assoc_location'),
]