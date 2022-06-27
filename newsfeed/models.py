from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField(max_length=255)
    content = RichTextUploadingField('Тело новости')
    # image = models.ImageField('Изображение', blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={"slug": self.slug})