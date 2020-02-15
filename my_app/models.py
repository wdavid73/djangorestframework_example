from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=150, null=True, blank=False)
    state = models.SmallIntegerField(default=1, null=False)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    cellphone = models.IntegerField()
    post = models.ManyToManyField(Post, through='AuthorPost')
    state = models.SmallIntegerField(default=1, null=False)

    def __str__(self):
        return self.name + ' - ' + self.cellphone


class AuthorPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    state = models.SmallIntegerField(default=1, null=False)
