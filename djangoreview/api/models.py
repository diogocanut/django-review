from django.db import models
from django.contrib.auth.models import User

RATING_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(
        choices=RATING_CHOICES, max_length=2, default='1')
    title = models.CharField(
        max_length=64,
        blank=False,
        null=False,
    )
    summary = models.TextField(
        blank=False,
        null=False,
        max_length=10000,
    )

    sub_date = models.DateTimeField('submission date', auto_now=True)
    ip_address = models.GenericIPAddressField(
        blank=True,
        null=True,
    )
    company_name = models.CharField(
        max_length=64,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
