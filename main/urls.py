from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home, name="home"),
    path('pricingandpayment/', v.pricing, name="pricing"),
]
