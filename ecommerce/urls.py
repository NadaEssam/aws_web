
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('products/<str:pk_test>/', views.products),
    path('users/<str:pk_test>/', views.users),
    path('orders/', views.orders),

    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    path('create_user/', views.createUser, name="create_user"),
    path('update_user/<str:pk>/', views.updateUser, name="update_user"),
    path('delete_user/<str:pk>/', views.deleteUser, name="delete_user"),

    path('create_product/', views.createProduct, name="create_product"),
    path('update_product/<str:pk>/', views.updateProduct, name="update_product"),
    path('delete_product/<str:pk>/', views.deleteProduct, name="delete_product"),

]
