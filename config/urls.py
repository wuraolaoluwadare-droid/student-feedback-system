from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Django's built-in admin
    path("admin/", admin.site.urls),

    # Student Portal
    path("", include("student_app.urls")),

    # Feedback Module
    path("", include("feedback_app.urls")),

    # Custom Administrator Portal
    path("administration/", include("admin_portal.urls")),

]