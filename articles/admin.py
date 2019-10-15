from django.contrib import admin

from .models import Post, Tag
from .forms import PostAdminForm


class PostAdmin(admin.ModelAdmin):

	class Meta:
		model = Post

	list_display = ['title', 'status', 'publish', 'language', 'is_active']
	list_editable = ['status', 'is_active']
	list_filter = ['status', 'is_active', 'tags']
	search_fields = ['title', 'content', 'description']

	list_per_page = 30

	form = PostAdminForm


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)