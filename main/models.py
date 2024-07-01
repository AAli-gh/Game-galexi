from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
import re
import uuid

phone_regex = RegexValidator(
    regex="^(?:(?:\+|00)98|0)?9\d{9}$",
    message="Please enter a valid Iranian phone number."
)

password_validator = RegexValidator(
    regex=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^\w\s]).{8,}$',
    message="Passwords must be at least 8 characters long and contain "
            "at least one digit, one lowercase letter, one uppercase "
            "letter, and one non-alphanumeric character.",
)

class UserProfile(models.Model):
    username = models.CharField(max_length=200, null=False, unique=True, blank=False)
    email = models.EmailField(max_length=50, null=False, unique=True, blank=False)
    fullname = models.CharField(max_length=20, null=False, blank=False)
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    password = models.CharField(max_length=128, validators=[password_validator], null=False)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    is_confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        digits_only = re.sub(r'\D', '', self.phone_number)
        if self.phone_number.startswith("98"):
            digits_only = "0" + digits_only[2:]
        formatted_number = digits_only.lstrip('0')
        self.phone_number = formatted_number
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
    
class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='games')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='games')
    categories = models.ManyToManyField(Category, related_name='games')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to='game_covers/', blank=True, null=True)
    trailer_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review of {self.game.title} by {self.user.username}'

class UserLibrary(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='library')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='user_libraries')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} owns {self.game.title}'


class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='orders')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order of {self.game.title} by {self.user.username} on {self.order_date}'

class Wishlist(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='wishlist')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='wishlist_entries')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} wishes for {self.game.title}'