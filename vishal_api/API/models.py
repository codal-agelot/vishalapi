from django.db import models

class Languages(models.Model):
    language = models.CharField(max_length=400,unique=True,null=True,blank=True)

    def __str__(self):
        return self.language


class Developers(models.Model):
    language = models.ManyToManyField(Languages,related_name='_language')
    # language = models.ForeignKey(Languages,on_delete=models.CASCADE)
    name = models.CharField(max_length=400,null=True,blank=True)

    def __str__(self):
        return  self.name


class Publication(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Article(models.model)
