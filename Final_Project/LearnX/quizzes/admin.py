from django.contrib import admin
from .models import Quiz, Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2  # show 2 empty fields by default


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # show 1 empty field by default


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title",)
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "quiz")
    search_fields = ("text",)
    inlines = [ChoiceInline]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("text", "question", "is_correct")
    list_filter = ("is_correct",)
    search_fields = ("text",)
