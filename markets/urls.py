from django.urls import path
from markets import views

app_name = "markets"
urlpatterns = [
    path("market_add/", views.market_add, name = "market_add"),
    path("<int:market_id>/", views.market_detail, name = "market_detail"),
]