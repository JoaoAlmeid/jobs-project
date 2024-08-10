from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("jobsApp.urls")),
    path('auth/', include('users.urls'))
]
