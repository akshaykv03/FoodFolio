"""
URL configuration for foodfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from foodapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('userReg', views.userReg),
    path('deliveryReg', views.deliveryReg),
    path('supplierReg', views.supplierReg),
    path('login', views.login),

    path('adminHome', views.adminHome),
    path('adminUser', views.adminUser),
    path('adminApproveUser', views.adminApproveUser),
    path('adminApproveSupplier', views.adminApproveSupplier),
    path('adminApproveDelivery', views.adminApproveDelivery),
    path('adminDelivery', views.adminDelivery),
    path('adminSupplier', views.adminSupplier),
    path('adminAdd', views.adminAdd),
    path('adminApproveFood', views.adminApproveFood),
    path('adminReport', views.adminReport),

    path('userHome', views.userHome),
    path('userFood', views.userFood),
    path('userCart', views.userCart),
    path('userCartView', views.userCartView),
    path('userRemove', views.userRemove),
    path('userPay', views.userPay),
    path('userBookings', views.userBookings),
    path('userFeedback', views.userFeedback),
    path('userReport', views.userReport),
    path('userGuidence', views.userGuidence),

    path('supplierHome', views.supplierHome),
    path('supplierAdd', views.supplierAdd),
    path('supplierOreder', views.supplierOreder),
    path('supplierGuidence', views.supplierGuidence),
    path('guidenceOpen', views.guidenceOpen),

    path('DeliveryHome', views.DeliveryHome),
    path('DeliveryOrder', views.DeliveryOrder),
    path('deliveryStatus', views.deliveryStatus),
    path('dBookingAccept', views.dBookingAccept),
    path('deliveryDelivered', views.deliveryDelivered),
    path('dBookingComplete', views.dBookingComplete),

]
