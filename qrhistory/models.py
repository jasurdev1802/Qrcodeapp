from django.db import models
from django.contrib.auth.models import User

class QRHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.TextField()
    type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.type}"