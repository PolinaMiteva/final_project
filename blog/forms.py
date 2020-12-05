from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_control()

    def form_control(self):
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_control()

    def form_control(self):
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Comment
        fields = '__all__'
