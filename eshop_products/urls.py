from django.urls import path
from .views import ProductList, product_detail, SearchProductsView, ProductListByCategory, products_categories_partial

urlpatterns = [
    path('products', ProductList.as_view()),
    path('products/<category_name>', ProductListByCategory.as_view()),
    path('products/<product_id>/<name>', product_detail),
    path('products/search', SearchProductsView.as_view()),
    path('products_categories_partial', products_categories_partial, name='product_categories_partial'),
]
