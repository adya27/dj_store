
from django.urls import path
from users.views import login, registration

app_name = 'products'

urlpatterns = [
    path('', login, name='login'),
    path('', registration, name='registration'),
]
