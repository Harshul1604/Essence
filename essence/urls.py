from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mainApp import views as mainApp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainApp.homePage),
    path('checkout/',mainApp.checkoutPage),
    path('shop/<str:mc>/<str:sc>/<str:br>/',mainApp.shopPage),
    path('contact/',mainApp.contactPage),
    path('single-product/<int:num>/',mainApp.singleProductPage),
    path('price-filter/<str:mc>/<str:sc>/<str:br>/',mainApp.priceFilterPage),
    path('sort-filter/<str:mc>/<str:sc>/<str:br>/',mainApp.sortFilterPage),
    path('search/',mainApp.searchPage),
    path('login/',mainApp.loginPage),
    path('signup/',mainApp.signupPage),
    path('logout/',mainApp.logoutPage),
    path('profile/',mainApp.profilePage),
    path('update-profile/',mainApp.updateProfilePage),
    path('add-to-cart/<int:num>/',mainApp.addToCartPage),
    path('cart/',mainApp.cartPage),
    path('delete-cart/<str:id>/',mainApp.deleteCartPage),
    path('update-cart/<str:id>/<str:op>/',mainApp.updateCartPage),
    path('place-order/',mainApp.placeOrderPage),
    path('confirmation/',mainApp.confirmationPage),
    path('add-to-wishlist/<int:num>/',mainApp.addToWishlistPage),
    path('delete-wishlist/<int:num>/',mainApp.deleteWishlistPage),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
