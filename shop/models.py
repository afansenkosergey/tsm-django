from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shopping_cart = models.ForeignKey('Order', null=True, blank=True, on_delete=models.SET_NULL,
                                      related_name='shopping_cart')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return self.user.username


class OrderEntry(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, default=None)
    count = models.PositiveIntegerField(default=1)
    order = models.ForeignKey('Order', related_name='entries', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.count} - {self.product.name}"


class Order(models.Model):
    class Status(models.TextChoices):
        INITIAL = 'INITIAL', 'Initial'
        COMPLETED = 'COMPLETED', 'Completed'
        DELIVERED = 'DELIVERED', 'Delivered'

    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.INITIAL)

    def __str__(self):
        return f"Order: {self.pk} - {self.profile.user.username}"
