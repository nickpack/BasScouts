from django.db import models
from django.db.models import permalink
from sorl.thumbnail.fields import ImageField

class FAQEntry(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __unicode__(self):
        return self.question

class ScoutPack(models.Model):
    title = models.CharField(max_length=255)
    uniform = ImageField(upload_to='uniforms')
    promise = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)

    def __unicode__(self):
        return self.title

    @permalink
    def get_news_url(self):
        return 'view_news_group', None, { 'slug': self.slug }

class ScoutLeader(models.Model):
    avatar = ImageField(upload_to='leaders')
    nickname = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    group = models.ManyToManyField(ScoutPack)

    def __unicode__(self):
        return self.nickname

class NewsCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return 'view_news_category', None, { 'slug': self.slug }

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    article_date = models.DateField()
    article_body = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ManyToManyField(NewsCategory)
    group = models.ManyToManyField(ScoutPack)

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return 'view_news_article', None, { 'slug': self.slug }

class Gallery(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

class GalleryImage(models.Model):
    image = ImageField(upload_to='galleries')
    title = models.CharField(max_length=255)
    group = models.ManyToManyField(ScoutPack)
    gallery = models.ForeignKey(Gallery)

    def __unicode__(self):
        return self.title