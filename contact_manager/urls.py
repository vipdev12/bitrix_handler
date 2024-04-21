from django.urls import path
from .views import webhook
urlpatterns = [
    path('webhook_handler/', webhook, name='webhook'),
]