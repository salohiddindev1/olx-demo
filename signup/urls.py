from django.urls import path
from signup.views import index_view, login_view, signup_view

urlpatterns = [
    path('', index_view),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
]