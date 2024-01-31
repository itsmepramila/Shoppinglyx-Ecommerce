from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from app.forms import LoginForm

urlpatterns = [
   path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="app/login.html", authentication_form=LoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    
    path('checkout/', views.checkout, name='checkout'),
]
