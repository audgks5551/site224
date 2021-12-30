from django.contrib import messages
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import (
    logout_then_login, LoginView,
)


# 라이브러리 및 커스텀
from .decorators import logout_required
from accounts.forms import SignupForm, FindForm
from lazy_string import LazyString
from accounts.models import User


class MyLoginView(SuccessMessageMixin, LoginView):
    template_name = "accounts/signin.html"
    next_page = "/"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.success_message = LazyString(
            lambda: f'{self.request.user.last_name}{self.request.user.first_name}님 환영합니다.')

    def get_initial(self):
        initial = self.initial.copy()
        initial['username'] = self.request.GET.get('username', None)

        return initial


@logout_required
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "회원가입 환영합니다.")
            next_url = request.GET.get('next', '/')
            print(request.GET.get('next', '/'))
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@logout_required
def signin(request: HttpRequest):
    return MyLoginView.as_view()(request)


def signout(request: HttpRequest):
    messages.success(request, "로그아웃 되었습니다.")
    return logout_then_login(request)


@logout_required
def getID(request: HttpRequest):
    if request.method == 'POST':
        form = FindForm(request.POST)
        if form.is_valid():
            print(form)
            email = request.POST.get("email")
            try:
                user = User.objects.get(email=email)
                user_username = user.username
                messages.success(request, f"회원님의 아이디는 {user_username} 입니다")
                return redirect('accounts:login')
            except User.DoesNotExist:
                messages.success(request, f"이메일이 일치하지 않습니다")
                form = FindForm()
                return redirect('accounts:find')
    else:
        form = FindForm()
    return render(request, 'accounts/find.html', {'form': form})
