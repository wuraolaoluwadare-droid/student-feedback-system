from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from student_app.models import Student


def home(request):
    return render(request, "student_app/home.html")


def login_view(request):

    if request.method == "POST":

        matric_no = request.POST.get("matric_no")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=matric_no,
            password=password
        )

        if user is not None:

            if user.is_staff:
                messages.error(
                    request,
                    "Please use the Admin portal."
                )
                return redirect("login")

            login(request, user)
            return redirect("dashboard")

        messages.error(
            request,
            "Invalid Matric Number or Password."
        )

    return render(request, "student_app/login.html")


@login_required
def dashboard(request):

    student = Student.objects.get(user=request.user)

    from feedback_app.models import Feedback, AnonymousComplaint
    from course_app.models import Course

    feedback_count = Feedback.objects.filter(student=student).count()

    complaint_count = AnonymousComplaint.objects.count()

    course_count = Course.objects.count()

    context = {
        "student": student,
        "feedback_count": feedback_count,
        "complaint_count": complaint_count,
        "course_count": course_count,
    }

    return render(
        request,
        "student_app/dashboard.html",
        context
    )


@login_required
def profile(request):

    student = Student.objects.get(user=request.user)

    return render(
        request,
        "student_app/profile.html",
        {
            "student": student
        }
    )


@login_required
def logout_view(request):
    logout(request)
    return redirect("home")