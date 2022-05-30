from django.contrib import admin
from .models import Bookclub
# Register your models here.


admin.site.register(Bookclub)

# class AdminBookclub(admin.ModelAdmin):
#     list_display = ('title', 'author', 'description', 'rating', 'created_at', 'updated_at')
#     list_filter = ('author', 'created_at', 'updated_at')
#     search_fields = ('title', 'author', 'description', 'rating')