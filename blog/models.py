from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    validation_list=['.jpg', '.png', '.jpeg']
    if not ext.lower() in validation_list:
        raise ValidationError('This Format Does Not Supported')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='file/user_avatar', null=False, blank=False, validators=[validate_file_extension])
    description = models.CharField(max_length=512, null=False, blank=False)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='file/article_cover', null=False,blank=False, validators=[validate_file_extension])
    content = RichTextField()
    created_at = models.DateField(default=datetime.now)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    promote = models.BooleanField(default=False)


class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='file/category_cover', null=False, blank=False, validators=[validate_file_extension])

    def __str__(self):
        return self.title


