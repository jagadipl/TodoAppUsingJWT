from django.urls import path,include
from . import views
from .views import LogoutView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('',views.homepage,name='homepage'),
  
    path('api/auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('todos/',views.TodoListCreateView.as_view(),name='todo-list-create'),
    path('todos/<int:pk>',views.TodoDetailView.as_view(),name='todo-detail'),
    path('logout/',LogoutView.as_view(),name='logout'),


]
