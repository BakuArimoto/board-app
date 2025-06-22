from django.shortcuts import render
from django.shortcuts import redirect
from . import forms

def home(request):
    return render(request, 'accounts/home.html')


def regist(request):
    regist_form = forms.RegistForm(request.POST or None)
    #POSTメソッドで送信された場合
    if regist_form.is_valid():
        regist_form.save(commit=True)
        return redirect('accounts:home')
    #GETメソッドで送信された場合
    return render(
        request, 'accounts/regist.html', context={
            'regist_form': regist_form,
        }
    )