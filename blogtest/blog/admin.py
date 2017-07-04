from django.contrib import admin

from .models import Post, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Пост', {'fields': ['title']}),
        (None, {'fields': ['content']}),
        (None, {'fields': ['datetime']}),
    ]
    inlines = [CommentInline]


admin.site.register(Post, PostAdmin)
