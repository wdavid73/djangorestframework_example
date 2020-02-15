from django.db import models

list_status = [
    (0, 'Inactive'),
    (1, 'Active')
]


class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=150, null=True, blank=False)
    state = models.CharField(max_length=10, null=False, blank=False, choices=list_status, default=1)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    cellphone = models.IntegerField()
    post = models.ManyToManyField(Post, through='Details')
    state = models.CharField(max_length=10, null=False, blank=False, choices=list_status, default=1)

    def __str__(self):
        return self.name


class Details(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reference = models.CharField(max_length=150, blank=False)
    state = models.CharField(max_length=10, null=False, blank=False, choices=list_status, default=1)
