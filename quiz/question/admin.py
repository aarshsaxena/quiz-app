from django.contrib import admin
from question.models import Question,QuizSession

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display=('text','option_a','option_b','option_c','option_d','correct_option')

admin.site.register(Question,QuestionAdmin)

class QuizSessionAdmin(admin.ModelAdmin):
    list_display=('nickname','total_questions','correct_answers','incorrect_answers')
admin.site.register(QuizSession,QuizSessionAdmin)
