from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Customize as needed
    search_fields = ('title', 'content')  # Optional: add search functionality




