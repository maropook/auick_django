from django.core import validators
from django.core.validators import RegexValidator
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

# Create your models here.


class Book(models.Model):
    isbn = models.CharField(
        verbose_name='ISBNコード',
        max_length=20,
        validators=[
            RegexValidator(
                r'978-4-[0-9]{4}-[0-9]{4}-[0-9]{1}$',
                message='正しい形式で指定してください')
        ]

    )
    title = models.CharField(
        verbose_name='著名',
        max_length=100
    )
    price = models.IntegerField(
        verbose_name='価格',
        default=0,
        validators=[
            MinValueValidator(
                17,
                message='正の整数で指定'
            )])
    publisher = models.CharField(
        verbose_name='出版社',
        max_length=50,
        choices=[('照英社', '照英社'),
                 ('技術評論社', '技術評論社'),
                 ('照英社', '照英社'),
                 ('技術評論社', '技術評論社'),
                 ('技術評論社', '技術評論社'),
                 ],
    )
    published = models.DateField(
        verbose_name='刊行日'
    )

    def get_absolute_url(self):
        return f'details/{self.id}'

    def __str__(self):
        return f'{self.title}({self.publisher}/{self.price}円)'


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(
        verbose_name='名前',
        max_length=20
    )
    body = models.TextField(
        verbose_name='本文',
        max_length=255
    )

    def __str__(self):
        return f'{self.name}:{self.body[:10]}'


class Author(models.Model):
    books = models.ManyToManyField(Book)
    name = models.CharField(
        verbose_name='名前',
        max_length=20
    )
    address = models.CharField(
        verbose_name='住所',
        max_length=100
    )

    def __str__(self):
        return self.name
