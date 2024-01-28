from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('vacancies/', views.VacancyListView.as_view(), name='vacancies'),
]
