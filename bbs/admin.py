from django.contrib import admin
from .models import Profile, Question
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Profile)#관리자가 수정할 수 있게