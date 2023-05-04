from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.authtoken.views import ObtainAuthToken
router=DefaultRouter()
router.register("register",views.UserView,basename="register"),
router.register("cakes",views.CakeView,basename="cake-list"),
# router.register("cakes/<int:pk>/addto-cart/",views.AddCartView,basename="addto-cart"),
router.register("carts",views.CartlistView,basename="list-cart")
router.register("reviews",views.ReviewlistView,basename="review")
urlpatterns = [
   path("token/",ObtainAuthToken.as_view(),name='user_token'),
   # path("cakes/<int:pk>/addto-cart/",views.AddCartView.as_view())
]+router.urls