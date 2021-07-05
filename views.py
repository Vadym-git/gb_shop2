from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from .models import UserModel


def index(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        return render(request, "email.html", {'form': ContactForm()})

    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['re_password']:
            try:
                check_user = UserModel.check_registration(form.cleaned_data['from_email'])
                if not check_user:
                    reg_link = UserModel.new_link(128)
                    # знаю что можно написать метод для регистрации юзера, оставляю на потом, чтоб было интересней
                    new_user = UserModel()
                    new_user.name = form.cleaned_data['from_email']
                    new_user.password = form.cleaned_data['re_password']
                    new_user.activation_link = reg_link
                    send_mail(
                        'You registration on my amazing website',
                        f'You did it: http://127.0.0.1:8000/registration/reg/{reg_link}',
                        from_email='noreply@****.eu',
                        recipient_list=['vadim.melnichenko@gmail.com'],
                    )
                    new_user.save()
                else:
                    return HttpResponse('Вы уже зарегистрированы')
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return HttpResponse('Линк для регистрации отправлен на ваш имейл')
        return HttpResponse('Something wrong with your form')


def confirmation_reg(response, slug=None):
    if not slug:
        return HttpResponse('Где твой код проверки????')
    check = UserModel.activation_user(slug)
    if check:
        return HttpResponse('Вы успешно зарегистрированы')
    return HttpResponse('Я тебя знать не знаю')
