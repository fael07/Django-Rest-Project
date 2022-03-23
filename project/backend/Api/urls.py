from django.urls import path

from .views.categories import CategoryCreateAndListView, CategoryDetailView, FilterCategoryView
from .views.products import FilterProductView, ProductCreateAndListView, ProductDetailView


urlpatterns = [
    path('products', ProductCreateAndListView.as_view()),
    path('products/filter', FilterProductView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view()),
    path('categories', CategoryCreateAndListView.as_view()),
    path('categories/filter', FilterCategoryView.as_view()),
    path('categories/<int:pk>', CategoryDetailView.as_view()),
]
