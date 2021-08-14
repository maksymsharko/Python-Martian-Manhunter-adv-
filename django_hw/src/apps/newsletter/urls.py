from django.urls import path

from src.apps.newsletter.views import NewNewsLetterView, SuccessTemplateView

app_name = 'newsletters'

urlpatterns = [
    path(
        'new/',
        NewNewsLetterView.as_view(),
        name='new_newsletter',
    ),
    path(
        'success/',
        SuccessTemplateView.as_view(),
        name='success',
    ),
]