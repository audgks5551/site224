from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from products.models import Product
from questions.models import Question
from .froms import QuestionForm
from accounts.models import User


# 질문 생성
def createQuestion(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = User.objects.last()
            question.object_id = product_id
            question.content_type = ContentType.objects.get(model='Question')
            question.save()
            return redirect('products:detail', product_id)
    else:
        form = QuestionForm()

    context = {'form': form, 'product': product}
    return render(request, 'question_create.html', context)

# 질문 보기


def showQuestion(request, product_id):

    question_list = Question.objects.filter(
        object_id=product_id, user=User.objects.last())
    context = {'question_list': question_list, 'product_id': product_id}
    return render(request, 'question_list.html', context)

# 질문 수정


def modifyQuestion(request, product_id, question_count):

    question_list = Question.objects.filter(
        object_id=product_id, user=User.objects.last())
    question = question_list[question_count-1]

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('products:questions:show', product_id)
    else:
        form = QuestionForm(instance=question)

    context = {'question_list': question_list, 'product_id': product_id,
               'form': form, 'question_count': question_count}
    return render(request, 'question_list.html', context)

# 질문 삭제


def deleteQuestion(request, product_id, question_count):
    question_list = Question.objects.filter(
        object_id=product_id, user=User.objects.last())
    question = question_list[question_count-1]
    question.delete()

    return redirect('products:questions:show', product_id)
