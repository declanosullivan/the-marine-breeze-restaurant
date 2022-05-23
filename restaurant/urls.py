from django.urls import path
from some_app.views import AboutView

urlpatterns = [
    path('menu/', MenuView.as_view()),
]