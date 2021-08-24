from django import forms
from datetime import date
from .models import Book


class BookForm(forms.Form):
    isbn = forms.CharField(label='ISBNコード', required=True, max_length=20)
    title = forms.CharField(label='署名', required=True, max_length=100)
    price = forms.IntegerField(label='価格', required=True, min_value=0)
    publisher = forms.ChoiceField(label='出版社',
                                  choices=[
                                      ('照英社', '照英社'),
                                      ('技術評論社', '技術評論社'),
                                      ('照英社', '照英社'),
                                      ('技術評論社', '技術評論社'),
                                      ('技術評論社', '技術評論社'),
                                  ])
    published = forms.DateField(label='刊行日', required=True)


class UploadForm(forms.Form):
    body = forms.FileField()


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('isbn', 'title', 'price', 'publisher', 'published')
