from django import forms
from django.contrib.auth.models import User

from Django_fnl_project.mixins import BootstrapFormControl
from blog.models import Post, Comment


class PostForm(forms.ModelForm, BootstrapFormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()
        self.fields['author'].queryset = User.objects.filter(
            groups__name__in=['writers', 'admin']) | User.objects.filter(is_superuser=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm, BootstrapFormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = Comment
        fields = 'user', 'post', 'body'
        widgets = {
            'body': forms.Textarea(),
        }
