from django.contrib import admin
from .models import BlogPost , Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','category','is_published','created_at','short_content')
    list_filter = ('is_published','category','created_at')
    search_fields = ('title','content')
    ordering = ('-created_at',)

    def short_content(self, obj):
        return obj.content[:50]