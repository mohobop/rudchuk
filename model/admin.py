from django.contrib import admin
from model.models import Head, Category, BodyText

# Register your models here.

class HeadInline(admin.StackedInline):
    model = Head
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    fields = ['category_title']
    inlines = [HeadInline]

admin.site.register(BodyText)
admin.site.register(Category, CategoryAdmin)