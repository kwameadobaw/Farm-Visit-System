from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.farm_visit_form, name='farm_visit_form'),
    path('visits/', login_required(views.farm_visit_list), name='farm_visit_list'),
    path('visits/<int:pk>/', login_required(views.farm_visit_detail), name='farm_visit_detail'),
    path('visits/<int:pk>/edit/', login_required(views.farm_visit_edit), name='farm_visit_edit'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]