from django.contrib import admin
from .models import *

admin.site.register(
    (
        Buyer,
        Maincategory,
        Subcategory,
        Brand,
        Product,
        Checkout,
        CheckoutProducts,
        Wishlist,
    )
)
