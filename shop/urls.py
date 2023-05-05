from django.urls import path
from .import orders,user,profile,collections,cart,fav,checkout

urlpatterns=[
    path("",user.home,name="home"),

    path("register",user.register,name="register"),
    path("login",user.login_page,name="login"),
    path("logout",user.logout_page,name="logout"),

    path("profile",profile.profile,name="profile"),
    path("new_profile",profile.new_profile,name="new_profile"),
    path("update_profile",profile.update_profile,name="update_profile"),
    path("update_password",profile.update_password,name="update_password"),

    path("product_list",collections.product_list,name="product_list"),
    path('search_product',collections.search_product,name="search_product"),

    path("collections",collections.collections,name="collections"),
    path("collections/<str:name>",collections.view,name="collections"),
    path("collections/<str:cname>/<str:pname>",collections.details,name="details"),

    path("addtocart",cart.addto_cart,name="addtocart"),
    path("cart",cart.cart_page,name="cart"),
    path("remove_cart/<str:cid>",cart.remove_cart,name="remove_cart"),

    path("fav",fav.fav,name="fav"),
    path("fav_page",fav.fav_page,name="fav_page"),
    path("remove_fav/<str:fid>",fav.remove_fav,name="remove_fav"),

    path("buy/<str:cname>/<str:pname>",checkout.buy,name="buy"),
    path("buy_placeorder",checkout.buy_placeorder,name="buy_placeorder"),

    path("checkout",checkout.checkout,name="checkout"),
    path("remove_checkout/<str:cid>",checkout.remove_checkout,name="remove_checkout"),
    path("placeorder",checkout.placeorder,name="placeorder"),

    path("my_orders",orders.my_orders,name="my_orders"),
    path("order_details/<str:oid>",orders.order_details,name="order_details"),
    path("cancel_order",orders.cancel_order,name="cancel_order"),
]
