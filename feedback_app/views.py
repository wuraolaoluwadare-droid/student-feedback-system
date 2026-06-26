from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Feedback, AnonymousComplaint
from course_app.models import Course
from student_app.models import Student


@login_required
def evaluation_form(request):
    courses = Course.objects.all()

    if request.method == "POST":

        course = Course.objects.get(id=request.POST["course"])
        student = Student.objects.get(user=request.user)

        if Feedback.objects.filter(student=student, course=course).exists():
            messages.error(
                request,
                "You have already submitted feedback for this course."
            )
            return redirect("evaluate")

        Feedback.objects.create(
            student=student,
            course=course,
            teaching_rating=request.POST["teaching_rating"],
            communication_rating=request.POST["communication_rating"],
            punctuality_rating=request.POST["punctuality_rating"],
            course_material_rating=request.POST["course_material_rating"],
            comment=request.POST["comment"]
        )

        messages.success(
            request,
            "Thank you! Your feedback has been submitted successfully."
        )

        return redirect("evaluate")

    return render(
        request,
        "feedback_app/evaluation_form.html",
        {"courses": courses}
    )


@login_required
def complaint_form(request):

    if request.method == "POST":

        AnonymousComplaint.objects.create(
            category=request.POST["category"],
            message=request.POST["message"]
        )

        messages.success(
            request,
            "Your complaint has been submitted anonymously."
        )

        return redirect("complaint")

    return render(
        request,
        "feedback_app/complaint_form.html"
    )


@login_required
def feedback_history(request):

    student = Student.objects.get(user=request.user)

    feedbacks = Feedback.objects.filter(student=student).order_by("-submitted_at")

    return render(
        request,
        "feedback_app/history.html",
        {
            "feedbacks": feedbacks
        }
    )