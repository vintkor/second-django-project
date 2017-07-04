from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField('Дата публикации')
    content = models.TextField('Текст')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    text_comment = models.TextField('Текст комментария')
    datetime = models.DateTimeField('Дата комментария')

    def __str__(self):
        return "Комментарий от {} для {}".format(self.datetime, self.post.title)
