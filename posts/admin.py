from django.contrib import admin
from .models import Category, Blog, Program, Event, Person
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ProgramAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('fullname',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Person, PersonAdmin)
