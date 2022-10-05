from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PersonalAccount.urls')),
    path('education/', include('Education.urls')),
    path('articles/', include('Articles.urls')),
]
