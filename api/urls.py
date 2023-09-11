from django.urls import path
from api import views


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'api'



urlpatterns = [
    path('', views.getRoutes,name='routes'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('allevents/',views.EventView.as_view()),
    path('event/',views.CrudEventView.as_view(), name="new event"),
    path('event/<int:pk>/',views.CrudEventView.as_view(), name="event"),
    path('availability/',views.AvailabilityView.as_view(), name="new availability"),
    #project urls
]