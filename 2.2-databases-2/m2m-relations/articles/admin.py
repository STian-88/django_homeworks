from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Relationship


class RelationshipInlineFormSet(BaseInlineFormSet):
    def clean(self):
        tags_dict = {}
        for form in self.forms:
            if form.cleaned_data['tag'] in tags_dict:
                raise ValidationError('Поворяющийся тег')
            tags_dict[form.cleaned_data['tag']] = form.cleaned_data['is_main']
        tags_list = [value for value in tags_dict.values() if value == True]
        if not tags_list:
            raise ValidationError('Выберите основной раздел')
        if len(tags_list) > 1:
            raise ValidationError('Основной раздел только один')
        return super().clean()

class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormSet
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline,
            ]
    list_display = ['title', 'published_at']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline,
            ]
