from django.urls import path

from base.views.advertisement import AdvertisementListView, AdvertisementDetailView
from base.views.auth import RegisterView, LoginView

urlpatterns = [
    path('advertisement-list/',
         AdvertisementListView.as_view(),
         name='advertisement_list'),
    path('advertisement-list/<int:advertisement_id>/',
         AdvertisementDetailView.as_view(),
         name='advertisement_detail'),
    path('auth/register/',
         RegisterView.as_view(),
         name='register'),
    path('auth/login/',
         LoginView.as_view(),
         name='login'),
]