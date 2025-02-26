from django.urls import path
from markets import views

app_name = "markets"
urlpatterns = [
    path("", views.market_list, name = "market_list"),
    path("add/", views.market_add, name = "market_add"),
    path("<int:id>/", views.market_detail, name = "market_detail"),
    # path("tags/<str: tag_name>/", views.nearby_tag_markets, name = "tag_search_list"),
    path("tags/<str:tag_name>/", views.nearby_tag_markets, name = "tag_search_list"),
]