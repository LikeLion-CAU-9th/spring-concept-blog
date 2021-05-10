from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    PUBLIC = 'public'
    PRIVATE = 'private'
    MY = 'my'

    SHOW_TYPES = [
        (PUBLIC, 'PUBLIC'),
        (PRIVATE, 'PRIVATE'),
        (MY, 'MY'),
    ]
    title = models.CharField(max_length=50, help_text='제목')
    show = models.CharField(max_length=10, choices=SHOW_TYPES, default=PUBLIC, help_text='post_type')
    body = models.TextField(help_text='내용')
    datetime = models.DateTimeField(default=timezone.now, help_text='작성시간')
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title