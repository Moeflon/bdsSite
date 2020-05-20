from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from . import views
from .views import home, dashboard, insights

urlpatterns = [
    path('', home, name='home'),
    path('dashboard', dashboard, name='dashboard'),
    path('insights', insights, name='insights')
]