from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', template_platform.as_view()),
    path('class/', class_template.as_view()),
    path('platform/cart/', template_cart.as_view()),
    path('platform/games/', games),
    path('platform/', template_platform.as_view()),
    path('platform/registration/', register_user),
    path('platform/news/', news),
    ]