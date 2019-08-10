from django.contrib import admin
from blogging.models import Post, Category


# create inline model admin to represent categories on the post admin view
class PostInLine(admin.TabularInline):

    model = Category.post.through


# create a customized ModelAdmin class for the post and category models
class PostAdmin(admin.ModelAdmin):

    inlines = [PostInLine,
               ]


class CategoryAdmin(admin.ModelAdmin):

    inlines = [PostInLine,
               ]
    exclude = ('posts',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)


