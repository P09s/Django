from django.contrib import admin
from.models import BlogDetail
admin.site.site_header = "BloGeeks Admin"
admin.site.index_title = "Blogs"
admin.site.site_title = "Blog administration"
admin.site.register(BlogDetail)

# Register your models here.
