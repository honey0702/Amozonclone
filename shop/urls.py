from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),
     path('product/<int:id>/', views.product_detail, name='product_detail'),
     path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
     path('cart/', views.cart, name='cart'),
     path('update-cart/<int:id>/<str:action>/', views.update_cart, name='update_cart'),
     path('catrgory/<str:name>/', views.category, name='category'),
     path('login/', views.login_view, name='login'),
     path('logout/' , views.logout_view, name='logout'),
]
