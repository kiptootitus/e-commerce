from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductListView, ProductDetailView,
    CategoryListView, CategoryDetailView,
    OrderListView, OrderDetailView,
    UserProfileDetailView, MessageViewSet, UserViewSet
)

router = DefaultRouter()
router.register(r'messages', MessageViewSet)
router.register(r'users', UserViewSet)
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # other URL patterns...
]

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('profiles/<int:pk>/', UserProfileDetailView.as_view(), name='user_profile'),
    path('', include(router.urls)),
]
