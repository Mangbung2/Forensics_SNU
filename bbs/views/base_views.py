from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from ..models import Question


def index(request):
    #입력인자
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')

    #정렬
    if so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')
    #조회
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        ).distinct()

    #페이징 처리
    paginator = Paginator(question_list, 5) #페이지당 5개
    page_obj = paginator.get_page(page)

    context = {'question_list' : page_obj, 'page':page, 'kw':kw, 'so':so}
    return render(
        request, 
        'bbs/question_list.html', 
        context
        )

def intro(request):
    return render(
        request,
        'bbs/intro.html'
    )

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(
        request,
        'bbs/question_detail.html',
        context
    )

def function(request):
        ce_option = request.GET.get('ce_option', '')
        #CE Option  
        if ce_option == '3130':
            print("3130")
        elif ce_option == '3500':
            print("3500")
        elif ce_option == 'SeqStudio':
            print("SeqStudio")
        else:
            print(ce_option)
        context = {'ce_option':ce_option}
        return render(
        request,
        'bbs/function.html',
        context
    )