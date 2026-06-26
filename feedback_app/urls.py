from django.urls import path
from . import views

urlpatterns = [
    path("evaluate/", views.evaluation_form, name="evaluate"),
    path("complaint/", views.complaint_form, name="complaint"),
    path("history/", views.feedback_history, name="history"),
]