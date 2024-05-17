from django.urls import path
from .views import shop_view
app_name = 'myshopapp'

urlpatterns = [
    path("", shop_view, name='shop_view')
]