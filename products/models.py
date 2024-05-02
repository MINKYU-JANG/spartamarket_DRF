from django.db import models
from accounts.models import CustomUser


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_login_required = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
