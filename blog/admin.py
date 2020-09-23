from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import Tag, Category, Post


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # формиурем слаг на основе тайтла
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    save_as = True

    #   кнопка наверху
    save_on_top = True
    # табличка постов в алминке
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo_list', 'views')
    # какие поля показывать внутри самой записи
    fields = ('title', 'slug', 'get_photo_list', 'photo', 'content', 'category', 'tags', 'created_at',)
    # делаем из полей ссылки на самих себя
    list_display_links = ('id', 'title',)
    # возможность поиска
    search_fields = ('title',)
    # фильтруем
    list_filter = ('category', 'tags')
    # поля только для чтения
    readonly_fields = ('views', 'created_at', 'get_photo_list',)

    @staticmethod
    def get_photo_list(obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="150">')
        else:
            return f'-'

    get_photo_list.short_description = 'Фото'


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
