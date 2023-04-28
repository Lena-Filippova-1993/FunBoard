from celery import shared_task
from django.contrib.auth.models import User
from .models import Post, Response
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone


@shared_task
def respond_send_email(respond_id):
    respond = Response.objects.get(id=respond_id)
    send_mail(
        subject=f'Доска объявлений: у Вас новый отклик!',
        message=f'Здравствуйте, дорогой(-ая) {respond.post.author}, ! На Ваше объявление есть новый отклик!\n'
                f'Прочитать отклик:\n http://127.0.0.1:8000/responses/{respond.post.id}',
        from_email='Lena-Filippova-93@yandex.ru',
        recipient_list=[respond.post.author.email, ],
    )


@shared_task
def respond_accept_send_email(response_id):
    respond = Response.objects.get(id=response_id)
    print(respond.post.author.email)
    send_mail(
        subject=f'Доска объявлений: Ваш отклик принят!',
        message=f'Здравствуйте, дорогой(-ая) {respond.author}, Автор объявления {respond.post.title} принял Ваш отклик!\n'
                f'Посмотреть принятые отклики:\nhttp://127.0.0.1:8000/responses',
        from_email='Lena-Filippova-93@yandex.ru',
        recipient_list=[respond.post.author.email, ],
    )


@shared_task
def send_mail_monday_8am():
    now = timezone.now()
    list_week_posts = list(Post.objects.filter(dateCreation__gte=now - timedelta(days=7)))
    if list_week_posts:
        for user in User.objects.filter():
            print(user)
            list_posts = ''
            for post in list_week_posts:
                list_posts += f'\n{post.title}\nhttp://127.0.0.1:8000/post/{post.id}'
            send_mail(
                subject=f'Доска объявлений: объявления за прошедшую неделю.',
                message=f'Здравствуйье, дорогой(-ая) {user.username}!\nПредлагаем Вам ознакомиться с новыми объявлениями, '
                        f'появившимися за неделю:\n{list_posts}',
                from_email='Lena-Filippova-93@yandex.ru',
                recipient_list=[user.email, ],
            )