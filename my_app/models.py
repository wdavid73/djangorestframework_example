from django.db import models

list_status = [
    ('Inactive', '0'),
    ('Active', '1')
]


class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=150, null=True, blank=False)
    # state = models.SmallIntegerField(default=1, null=False)
    state = models.CharField(max_length=10, null=False, blank=False, choices=list_status, default='Active')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    cellphone = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    state = models.CharField(max_length=10, null=False, blank=False, choices=list_status, default=1)

    def __str__(self):
        return self.name + ' - ' + self.cellphone
