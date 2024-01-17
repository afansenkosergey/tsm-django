from django import forms


from .models import Article, Author, Comment


class ArticleForm(forms.ModelForm):
    """
    Форма для создания и редактирования объектов модели Article.

    Meta:
        model (Article): Модель, связанная с формой.
        fields (list): Список полей, которые будут отображены в форме.

    """

    class Meta:
        model = Article
        fields = ['title', 'text']


class AuthorForm(forms.ModelForm):
    """
    Форма для создания и редактирования объектов модели Author.

    Meta:
        model (Author): Модель, связанная с формой.
        fields (list): Список полей, которые будут отображены в форме.

    """

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


class CommentForm(forms.ModelForm):
    """
    Форма для создания и редактирования объектов модели Comment.

    Meta:
        model (Comment): Модель, связанная с формой.
        fields (list): Список полей, которые будут отображены в форме.

    """

    class Meta:
        model = Comment
        fields = ['text']


