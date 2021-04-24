from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login/', user_views.UserLogin.as_view(), name='login'),
    path('logout/', user_views.UserLogout.as_view(), name='logout'),
]
