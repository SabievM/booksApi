from django.contrib import admin
from .models import Book, Author, Genre, Category, Cart

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "genre", "price", "is_new", "is_bestseller")
    list_filter = ("category", "genre", "is_new", "is_bestseller")
    search_fields = ("title", "author__name")
    ordering = ("title",)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "author_type")
    list_filter = ("author_type",)
    search_fields = ("name",)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "quantity")
    search_fields = ("user__username", "book__title")