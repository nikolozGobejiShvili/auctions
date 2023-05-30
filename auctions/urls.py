from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new/",views.post_create_view, name ="new_post"),
    path("posts/<int:pk>/", views.get_post_details, name="post-details"),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('add_watchlist/<int:pk>/', views.add_watchlist, name='add_watchlist'),
    path('remove_watchlist/<int:pk>/', views.remove_watchlist, name='remove_watchlist'),
    path('close_auction/<int:pk>/', views.close_auction, name='close-auction'),
    path("posts/<int:pk>/bid/", views.bid, name="bid"),
    path('categories/', views.category_list, name='category-list'),
    path('categories/<int:category_id>/', views.category_detail, name='category-detail'),
    path("posts/<int:pk>/add_comment/", views.add_comment, name="add_comment"),
    
]
