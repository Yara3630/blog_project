from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(
        max_length=20,
        default='Без названия')
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts')
    image = models.ImageField(
        blank=True,
        upload_to='posts/')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts')

    def __str__(self):
        return self.text[:15]

    class Meta:
        ordering = ('-pub_date',)


class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments')

    def __str__(self):
        return self.text[:15]

    class Meta:
        ordering = ('-pub_date',)


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followed')

    class Meta:
        constraints = (models.UniqueConstraint(
            fields=['user', 'author'],
            name='unique_follow'),)
