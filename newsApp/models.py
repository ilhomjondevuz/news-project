from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        ordering = ['-created_at']
        db_table = 'categories'

NewsCHOOCES = (
    ('DF', 'DRAFT'),
    ('PD', 'PENDING'),
    ('PB', 'PUBLISHED'),
    ('SC', 'SCHEDULED'),
    ('AR', 'ARCHIVED'),
    ('RE', 'REJECTED'),
    ('HD', 'HIDDEN')
)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='PB')

class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='news/photos/%Y/%m', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=NewsCHOOCES, default='DF')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = PublishedManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'
        verbose_name = 'News'
        ordering = ['-created_at']
        db_table = 'news'