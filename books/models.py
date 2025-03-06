from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    FOREIGN = "зарубежные"
    LOCAL = "отечественные"
    CHECHEN = "чеченские"

    AUTHOR_TYPES = [
        (FOREIGN, "Зарубежные"),
        (LOCAL, "Отечественные"),
        (CHECHEN, "Чеченские"),
    ]

    name = models.CharField(max_length=255, unique=True)
    author_type = models.CharField(max_length=20, choices=AUTHOR_TYPES)

    def __str__(self):
        return self.name

class Book(models.Model):
    COVER_TYPES = [("мягкий", "Мягкий"), ("твердый", "Твердый")]

    LANGUAGES = [
        ("русский", "Русский"),
        ("английский", "Английский"),
        ("арабский", "Арабский"),
        ("французский", "Французский"),
        ("немецкий", "Немецкий"),
        ("чеченский", "Чеченский"),
    ]

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    cover = models.CharField(max_length=10, choices=COVER_TYPES, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="books")
    year = models.PositiveIntegerField(blank=True, null=True)
    language = models.CharField(max_length=20, choices=LANGUAGES, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_new = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="books/", blank=True, null=True)

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"