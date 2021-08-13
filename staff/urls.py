from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', view=views.home, name='home'),
    path('login', view=views.handle_login, name='handle_login'),
    path('logout', view=views.handle_logout, name='handle_logout'),
    path('products', view=views.products, name='products'),
    path('analytics', view=views.analytics, name='analytics'),
    path('orders', view=views.orders, name='orders'),
    path('money', view=views.money, name='money'),





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
