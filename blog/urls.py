from django.urls import path
from .views import *


urlpatterns = [
    path("", home_page, name="home"),
    path("nav/", nav_page, name='nav'),
    path("footer/", footer_page, name='footer/'), 
    path("register/", register_page, name='register'),
    path("login/", login_page, name='login'),
    path("logaut/", logaut_page, name='logaut'),
    path("discount/", discount_page, name='discount'),
    path("sidebar/",sidebar_page, name='sidebar' ),
    path("gadjet/", gadjet_page, name='gadjet'),
    path("texnika/", texnika_page, name='texnika'),
    path("kitob/", kitob_page, name='kitob'),
    path("tv/", televizor_page, name='tv'),
    path("expensiv/", expensive_page, name='expensiv'),
    path("notebook/", notebook_page, name='notebook'),
    path("product/", search_page, name='search'), 
    path("cart/", shopingCart_page, name='shoppingCart'),
    path("buy/<str:tovar_id>/",buy_page, name='buy'),
    path("tovar/<str:tovar_id>/", tovar_page, name='tovar'),
    path("like/", like_page, name='like'),
    path("contact/", contact_page, name='contact'),
    path('add_to_cart/<str:tovarni_idsi>/', add_to_cart_page, name='add_to_cart'),
    path("add_to_like/<str:like_id>/", add_to_like_page, name='like' ),
    path("remove/<int:tovar_id>/", remove_page, name='remove'),
    path("remove/<int:like_id>/", remove_like_page, name='remove_like'),
]