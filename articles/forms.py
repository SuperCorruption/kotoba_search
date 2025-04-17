from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    tags = forms.CharField(
            required=False,
            label='タグ',
            help_text='例: a, b, c',
            widget=forms.TextInput(attrs={'class': 'form-control', 'placsholder': 'a, b, c'})
    )

    class Meta:
        model = Article
        fields = ['title', 'content', 'work_title', 'volume', 'episode', 'subtitle', 'page_number']
        labels = {
                'title': '語句',
                'work_title': '作品名',
                'volume': '巻数',
                'subtitle': 'サブタイトル',
                'page_number': 'ページ数',
                'content': '本文',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'work_title': forms.Select(attrs={'class': 'form-select'}),
            'volume': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'episode': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'page_number': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
