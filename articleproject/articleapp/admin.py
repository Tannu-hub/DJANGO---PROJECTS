from django.contrib import admin
from articleapp.models import ArticleModel


# Register your models here.
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','author','date']
admin.site.register(ArticleModel,ArticleModelAdmin)

