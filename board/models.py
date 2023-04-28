from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextField
from ckeditor.fields import RichTextField



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    CATEGORY = (
        ('tanks', 'Танки'),
        ('healers', 'Хилы'),
        ('dd', 'ДД'),
        ('dealers', 'Торговцы'),
        ('gildmasters', 'Гилдмастеры'),
        ('quest_givers', 'Квестгиверы'),
        ('blacksmiths', 'Кузнецы'),
        ('tanners', 'Кожевники'),
        ('potions_makers', 'Зельевары'),
        ('spell_masters', 'Мастера заклинаний')
    )
    category = models.CharField(max_length=15, choices=CATEGORY, verbose_name='Категория...')
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, verbose_name='Названик...')
#    text = TextField()
    text = RichTextField()

    def __str__(self):
        return f'Объявление: {self.title}: {self.text}'

class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отзыв {self.text} написал {self.author}'
