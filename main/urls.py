from django.urls import path
from . import views as v
from .views import QariListView, QariDetailView

urlpatterns = [
    path('', v.home, name="home"),
    path('pricingandpayment/', v.pricing, name="pricing"),
    path('qari/', QariListView.as_view(), name="teachers"),
    path('qari/<int:pk>', QariDetailView.as_view(), name = "qari")
]
