from django.urls import path

from api.views import RecognizePhoneView

urlpatterns = [
    path('recognition/', RecognizePhoneView.as_view()),
]
