from django.db import models
from student_app.models import Student
from course_app.models import Course


class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    teaching_rating = models.PositiveSmallIntegerField()
    punctuality_rating = models.PositiveSmallIntegerField()
    communication_rating = models.PositiveSmallIntegerField()
    course_material_rating = models.PositiveSmallIntegerField()

    comment = models.TextField(blank=True, null=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'course'],
                name='unique_student_course_feedback'
            )
        ]

    def __str__(self):
        return f"{self.student.full_name} - {self.course.course_code}"


class AnonymousComplaint(models.Model):
    CATEGORY_CHOICES = [
        ('Lecturer Misconduct', 'Lecturer Misconduct'),
        ('Harassment', 'Harassment'),
        ('Poor Facilities', 'Poor Facilities'),
        ('Examination Issues', 'Examination Issues'),
        ('Other', 'Other'),
    ]

    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.category
    
    
