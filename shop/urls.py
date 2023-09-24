from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView
urlpatterns=[
    
    path('', views.home,name="home") ,
    path('Register', views.Register,name="Register"),
    path('login', views.login_page,name="login"),
    path('logout', views.logout_page,name="logout"),
    path('checkout', views.checkout_page,name="checkout"),
    path('cart', views.cart_page,name="cart"),
    path('remove_cart/<str:cid>', views.remove_cart,name="remove_cart"),
    path('fav', views.fav_page,name="fav"),
    path('remove_fav/<str:fid>', views.remove_fav,name="remove_fav"),
    path('favviewpage', views.favviewpage,name="favviewpage"),
    path('addtocart', views.add_to_cart,name="addtocart"),
    path('collection', views.collection,name="collection"),
    path('collection/<str:name>', views.collectionview,name="collection"),
    path('collection/<str:cname>/<str:pname>', views.productdetails,name="productdetails"),
    path('password_reset/',PasswordResetView.as_view(),name="password_reset"),
    path('password_reset_done/',PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]