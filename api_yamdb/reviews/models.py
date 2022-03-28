from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User

from api_yamdb.settings import THIS_YEAR


class Category(models.Model):
    name = models.CharField(max_length=64,
                            verbose_name='Название категории')
    slug = models.SlugField(max_length=64, unique=True,
                            verbose_name='Идентификатор категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Genre(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Название жанра')
    slug = models.SlugField(max_length=64, unique=True,
                            verbose_name='Идентификатор жанра')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['id']


class Title(models.Model):
    name = models.CharField(max_length=64,
                            verbose_name='Название произведения')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='titles',
                                 verbose_name='Категория произведения')
    genre = models.ManyToManyField(Genre,
                                   related_name='titles',
                                   verbose_name='Жанр произведения')
    year = models.IntegerField(verbose_name='Год выхода произведения')
    description = models.TextField(blank=True,
                                   verbose_name='Описание произведения')

    def clean(self):
        if not 0 < self.year <= THIS_YEAR:
            raise ValidationError(
                f'Год должен быть больше 0 и меньше {THIS_YEAR}!'
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['id']


class Review(models.Model):
    text = models.TextField(verbose_name='Текст отзыва')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='reviews',
                               verbose_name='Автор отзыва')
    score = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ], verbose_name='Оценка произведения'
    )
    title = models.ForeignKey(Title,
                              on_delete=models.CASCADE,
                              related_name='reviews',
                              verbose_name='Произведение')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    db_index=True,
                                    verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review'
            )
        ]

    def __str__(self):
        return self.text


class Comments(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='Автор комментария')
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True,
                                    db_index=True,
                                    verbose_name='Дата добавления')
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='Отзыв')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['id']

    def __str__(self):
        return self.text
