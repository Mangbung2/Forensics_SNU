from django import forms
from django.forms import fields, widgets
from bbs.models import Profile, Question, Answer, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'level'
        ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'subject',
            'content',
            'category',
            'uploadedFile',
        ]
        labels = {
            'subject':'제목',
            'content':'내용',
            'category':'카테고리',
            'uploadedFile':'파일업로드'
        }
        

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'content'
        ]
        labels = {
            'content':'답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content':'댓글내용',
        }