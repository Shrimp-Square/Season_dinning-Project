from django.urls import path
from markets import views

app_name = "markets"
urlpatterns = [
    path("", views.market_list, name = "market_list"),
    path("add/", views.market_add, name = "market_add"),
    path("<int:market_id>/", views.market_detail, name = "market_detail"),
    # path("tags/<str: tag_name>/", views.nearby_tag_markets, name = "tag_search_list"),
    path("tags/<str:tag_name>/", views.nearby_tag_markets, name = "tag_search_list"),
    path("<int:market_id>/like/", views.market_like, name = "market_like"),
    path("<int:market_id>/comment_add/", views.comment_add, name="comment_add"),
    path("<int:market_id>/edit/", views.market_edit, name = "market_edit"),
    path("<int:comment_id>/comment_delete/", views.comment_delete, name = "comment_delete"),
    path("<int:market_id>/delete/", views.market_delete, name = "market_delete"),
]