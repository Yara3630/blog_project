from django import forms
from . models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'group', 'image')
        labels = {'title': 'Заголовок поста',
                  'text': 'Текст нового поста',
                  'group': 'Тематическая группа',
                  'image': 'Картинка'}
        help_texts = {'title': 'Введите заголовок',
                      'text': 'Введите текст поста',
                      'group': 'Выберите группу',
                      'image': 'Загрузите картинку'}

    def clean_text(self):
        data = self.cleaned_data['text']
        if data == '':
            raise forms.ValidationError('Текст не должен отсутствовать')
        return data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': 'Текст комментария'}
        help_text = {'text': 'Введите текст комменария'}

    def clean_text(self):
        data = self.cleaned_data['text']
        if data == '':
            raise forms.ValidationError('Текст не должен отсутствовать')
        return data


class SearchForm(forms.Form):
    query = forms.CharField(label='',
                            max_length=50,
                            required=False,
                            widget=forms.TextInput(attrs={
                                'placeholder': 'Поиск по сайту...',
                                'class': 'form-control search-input',
                                'aria-label': 'Поиск'
                            }))
