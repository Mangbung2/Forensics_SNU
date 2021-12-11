from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect(
                'bbs:index'
            )
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(
        request,
        'bbs/question_form.html',
        context
    )

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('bbs:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST,request.FILES, instance=question)
        
        #a = request.FILES['uploadedFile'].size
        a = request.FILES.get('uploadedFile')
        if a != None:
            a = a.read()
            a = len(a)
            size = a/1024/1024
            if size > 30:
                messages.error(request, '파일 사이즈가 너무 큽니다.(현재 %.2fMB)'%size)
                return redirect(request.path, question_id=question.id)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('bbs:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form':form}
    return render(
        request, 
        'bbs/question_form.html', 
        context
        )

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('bbs:detail', question_id=question.id)
    question.delete()
    return redirect('bbs:index')

