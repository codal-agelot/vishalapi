from django.urls import path,include
from .api import router
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vishal_api/',include(router.urls)),
    # path('vishal_api/auth/', include('djoser.urls.authtoken')),

]