from django.contrib import admin

from article.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'tag_list', 'author']

    class Meta:
        model = Article

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(Article, ArticleAdmin)
