from django.contrib import admin
from .models import Post, Votes

class PostAdminLayout(admin.ModelAdmin):
    readonly_fields = ('upvotes', 'downvotes')

class VotesAdminLayout(admin.ModelAdmin):
    readonly_fields = ('post', 'user')

admin.site.register(Post, PostAdminLayout)
admin.site.register(Votes, VotesAdminLayout)