from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Gig(models.Model):
    title        = models.CharField(max_length=100)
    description  = models.TextField()
    amount       = models.DecimalField(max_digits=10, decimal_places=2)
    created_by   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gigs')
    date_posted  = models.DateTimeField(auto_now_add=True)
    favorited_by = models.ManyToManyField(User, related_name='favorite_gigs', blank=True)

    def __str__(self):
        return self.title
