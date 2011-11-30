from sujets.models import *
from django.contrib import admin

class OptionInline(admin.TabularInline):
    model = Option
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Question, QuestionAdmin)

class OptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'question')
    list_filter = ('question', )

admin.site.register(Option, OptionAdmin)
