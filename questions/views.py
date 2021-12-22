from django.contrib import auth
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from products.models import Product
from .froms import QuestionForm
from accounts.models import User
# Create your views here.


def createQuestion(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.object_id = product_id
            user = User.objects.last()  # 임시
            question.user = user
            question.content_type = ContentType.objects.get(model='Question')
            question.save()
            return redirect('products:detail', product_id)
    else:
        form = QuestionForm()

    form = QuestionForm()
    context = {'form': form, 'product': product}
    return render(request, 'question_create.html', context)
