from .views import HomeView,ItemDetailView,SubCategory,SearchView,signup,cart
from django.urls import path
app_name='home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>',ItemDetailView.as_view(), name='product'),
    path('subcategory/<id>',SubCategory.as_view(), name='subcategory'),
    path('cart/<slug>',cart(), name='cart'),
    path('search',SearchView.as_view(), name='search'),
    path('signup', signup, name='signup'),
    path('mycart', CartView.as_view(), name='mycart'),
    0

]
