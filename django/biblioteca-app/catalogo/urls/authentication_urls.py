from django.urls import path
from catalogo.views.authentication_views import BiliotecaLoginView, BibliotecaLogoutView

urlpatterns = [
    path('login/', BiliotecaLoginView.as_view(), name='login'),
    path('logout/', BibliotecaLogoutView.as_view(), name='logout'),
]