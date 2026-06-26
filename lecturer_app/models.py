from django.db import models

class Lecturer(models.Model):
    lecturer_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name