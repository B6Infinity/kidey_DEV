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

    # APIs
    path('add-product', view=views.addProduct, name='add-product'),
    path('delete-product', view=views.deleteProduct, name='delete-product'),
    path('add-order', view=views.addOrder, name='add-order'),
    path('delete-order', view=views.deleteOrder, name='delete-order'),
    path('withdrawMoney', view=views.withdrawMoney, name='withdrawMoney'),
    path('fetchCustomer', view=views.fetchCustomer, name='fetchCustomer'),
    path('fetchOrder', view=views.fetchOrder, name='fetchOrder'),
    path('markOrderPaid', view=views.markOrderPaid, name='markOrderPaid'),
    path('editCustomer', view=views.editCustomer, name='editCustomer'),
    path('deleteCustomer', view=views.deleteCustomer, name='deleteCustomer'),
    path('deleteExpense', view=views.deleteExpense, name='deleteExpense'),

    path('add-landmark', view=views.addLandmark, name='add-landmark'),
    path('delete-landmark', view=views.deleteLandmark, name='delete-landmark'),

    # STATICITY

    path('get_menu', view=views.get_menu, name='get_menu'),
    path('get_landmark_details', view=views.get_landmark_details, name='get_landmark_details'),
    path('respond_avail', view=views.respond_avail, name='respond_avail'),
    path('fetchMenu', view=views.fetchMenu, name='fetchMenu'),
    path('fetchDeliveryRateChart', view=views.fetchDeliveryRates, name='fetchDeliveryRates'),

    path('pushOrders__STATIC', view=views.addOrders__STATICPUSH, name='pushOrders__STATIC'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
