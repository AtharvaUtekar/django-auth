
# iveri/urls.py
from django.urls import path
from .views import PersonalDetailsView
app_name = 'iveri'

urlpatterns = [
    path('personal-details/', PersonalDetailsView.as_view(), name='personal-details'),
]