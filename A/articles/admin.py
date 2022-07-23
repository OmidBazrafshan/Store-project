from django.contrib import admin
from articles.models import Article ,Sefaresh

class ArticleAdmin(admin.ModelAdmin):
    list_display =['id','item','price','image','is_active','discription']

class SefareshAdmin(admin.ModelAdmin):
    list_display =['id','firstname','lastname','number',]


admin.site.register(Article , ArticleAdmin)

admin.site.register(Sefaresh , SefareshAdmin)
