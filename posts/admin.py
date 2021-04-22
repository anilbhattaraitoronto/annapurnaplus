from django.contrib import admin
from .models import Category, Blog, Program, Event, Person, Presentation
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category',
                    'created_date', 'is_archived', 'is_featured']
    list_editable = ('is_archived', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}


class ProgramAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'director')


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date']
    prepopulated_fields = {'slug': ('title',)}


class PersonAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'role_choice', 'added_date')
    list_editable = ['role_choice', ]
    prepopulated_fields = {'slug': ('fullname',)}


class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'person', 'document')
    list_editable = ['document', ]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Presentation, PresentationAdmin)
