from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from .managers import PublishedManager


class Newness(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", _("Draft")
        PUBLISHED = "PB", _("Published")

    title = models.CharField(
        max_length=200,
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        primary_key=True,
    )
    content = models.TextField()

    photo = models.ImageField(
        upload_to="news/%Y/%m/%d",
    )

    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="news",
    )

    published_at = models.DateTimeField(
        default=timezone.now,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    objects = models.Manager()  # default manager
    published_objects = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_at"]
        db_table = "news"
        verbose_name = _("News")
        verbose_name_plural = _("News")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Newness, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(
        max_length=200,
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        primary_key=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-title"]
        db_table = "categories"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)