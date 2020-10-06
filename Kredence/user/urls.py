from django.urls import path
from .views import (
    signup_view,
    activation_sent_view,
    activate,
    home_view,
    login_view
)

urlpatterns = [
    path('', home_view, name="home"),
    path('signup/', signup_view, name="signup"),
    path('signin/', login_view, name="login"),
    path('activation-sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]
