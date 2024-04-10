from django.urls import path

from products import views
# from products.views import (
#     CategoryListAPIView,
#     CategoryDetailAPIView,
#     ProductListAPIView,
#     ProductDetailAPIView,
#     ReviewListAPIView,
#     ReviewDetailAPIView,
#     ProductReviewListAPIView
# )

urlpatterns = [
    path('categories/', views.category_list_api_view),
    path('categories/<int:id>/', views.category_detail_api_view),
    path('products/', views.product_list_api_view),
    path('products/<int:id>/', views.product_detail_api_view),
    path('reviews/', views.review_list_api_view),
    path('reviews/<int:id>/', views.review_detail_api_view),
    path('products/reviews/', views.product_review_list_api_view)
]

# urlpatterns = [
#     path('categories/', CategoryListAPIView.as_view()),
#     path('products/categories/<int:pk>/', CategoryDetailAPIView.as_view()),
#     path('products/', ProductListAPIView.as_view()),
#     path('products/<int:pk>/', ProductDetailAPIView.as_view()),
#     path('reviews/', ReviewListAPIView.as_view()),
#     path('reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
#     path('products/reviews/', ProductReviewListAPIView.as_view()),
# ]