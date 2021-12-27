from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from products.models import Product, ProductReal
from questions.models import Question
from .froms import QuestionForm
from accounts.models import User
from django.contrib.auth.decorators import login_required


# 질문 생성
@login_required(login_url='accounts:login')
def createQuestion(request, product_id):
    user_id = request.user.id
    product = Product.objects.get(id=product_id)
    product_reals = ProductReal.objects.filter(product=product)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = User.objects.get(id=user_id)
            question.object_id = product_id
            question.content_type = ContentType.objects.get(model='Product')
            question.save()
            return redirect('products:detail', product_id)
    else:
        form = QuestionForm()

    context = {'form': form, 'product': product,
               'product_reals': product_reals}
    return render(request, 'question_create.html', context)


# 내 질문 보기


@login_required(login_url='accounts:login')
def showQuestion(request, product_id):
    user_id = request.user.id
    question_list = Question.objects.filter(
        object_id=product_id, user=User.objects.get(id=user_id))
    context = {'question_list': question_list, 'product_id': product_id}
    return render(request, 'question_list.html', context)

# 내 질문 수정


@login_required(login_url='accounts:login')
def modifyQuestion(request, product_id, question_count):
    user_id = request.user.id
    question_list = Question.objects.filter(
        object_id=product_id, user=User.objects.get(id=user_id))
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


@login_required(login_url='accounts:login')
def deleteQuestion(request, product_id, question_count):
    user_id = request.user.id
    question_list = Question.objects.filter(
        object_id=product_id, user=User.objects.get(id=user_id))
    question = question_list[question_count-1]
    question.delete()

    return redirect('products:questions:show', product_id)
