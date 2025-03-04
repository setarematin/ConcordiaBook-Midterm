from django.db import models


class TextBook(models.Model):
    CONDITION_CHOICES = [
        ("new", "New"),
        ("written", "Written"),
        ("old", "Old"),
    ]

    title = models.CharField(max_length=255)
    year = models.IntegerField()
    edition = models.CharField(max_length=50, null=True, blank=True)
    author = models.CharField(max_length=255)
    course_code = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
