#coding=utf-8
from django.shortcuts import render
from wenda.models import *
from django.shortcuts import render_to_response
from wenda.forms import CommentForm
from django.http import Http404
# Create your views here.
# def index(request):
#     question_list = Question.objects.all()
#     return render_to_response('index.html',{'question_list':question_list})
def get_questions(request):
    questions = Question.objects.all().order_by('-created')
    return render_to_response('question_list.html',{'questions':questions})

def get_details(request,question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['question'] = question
            Comment.objects.create(**cleaned_data)
    ctx = {
        'question':question,
        'comments':question.comment_set.all().order_by('-created'),
        'form':form
    }
    return render(request,'question_details.html',ctx)
def Login(request):
    return render(request,'login.html')
