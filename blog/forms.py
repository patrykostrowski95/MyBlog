from django import forms
from blog.models import Post, Comment, UserProfileInfo
from django.contrib.auth.models import User



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'image', 'video')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')


# USER FORM

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class UserProfileInfoForm (forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('profile_pic',)
