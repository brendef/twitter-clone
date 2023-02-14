from django.contrib import admin
from .models import Post, Vote

class PostAdminLayout(admin.ModelAdmin):
    readonly_fields = ('upvotes', 'downvotes')

class VoteAdminLayout(admin.ModelAdmin):
    readonly_fields = ('post', 'user')

admin.site.register(Post, PostAdminLayout)
admin.site.register(Vote, VoteAdminLayout)