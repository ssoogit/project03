from django.contrib import admin
from .models import MainContent,Comment
from .models import MyModel

class MainContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date']
    search_fields = ['title']
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']

class MyModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']


admin.site.register(MainContent, MainContentAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(MyModel, MyModelAdmin)
