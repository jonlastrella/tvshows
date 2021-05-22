from django.db import models

# Create your models here.


class ShowManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters."
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters."
        return errors


class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
