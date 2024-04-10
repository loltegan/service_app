from django.contrib import admin
from django.urls import path
from rest_framework import routers

from services.views import SubscriptionViews

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register(r'api/subscription', SubscriptionViews)

urlpatterns += router.urls
