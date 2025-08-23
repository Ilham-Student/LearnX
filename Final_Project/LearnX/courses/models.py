from django.db import models

from django.db import models

class Course(models.Model):
    SKILL_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    skill_level = models.CharField(max_length=20, choices=SKILL_LEVELS, default='beginner')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# courses/models.py
from django.db import models
from .models import Course  # if Course is in the same app

class Video(models.Model):
    course = models.ForeignKey(Course, related_name="videos", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    youtube_url = models.URLField(blank=True, null=True)


    def get_embed_url(self):
        """
        Convert a normal YouTube link into an embeddable one.
        Example:
        https://www.youtube.com/watch?v=abcd1234 → https://www.youtube.com/embed/abcd1234
        """
        if "watch?v=" in self.youtube_url:
            video_id = self.youtube_url.split("watch?v=")[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        elif "youtu.be/" in self.youtube_url:
            video_id = self.youtube_url.split("youtu.be/")[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        return self.youtube_url


