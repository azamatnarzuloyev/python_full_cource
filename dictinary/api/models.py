from django.db import models

from ckeditor.fields import RichTextField

from django.utils.text import slugify
import random, string
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Worlds(models.Model):
    world = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, editable=False, null=False, blank=True)
    translation= models.TextField(blank=True, null=True)
    info = RichTextField(verbose_name='info', blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    # data = models.DateField(auto_created=True)

    @property
    def url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    @property
    def has_banner_ad(self):
        if self.banner_ad:
            return True
        return False

    @classmethod
    def make_slug(cls, world):
        slug = slugify(world, allow_unicode=False)
        letters = string.ascii_letters + string.digits

        while cls.objects.filter(slug=slug).exists():
            slug = slugify(
                world + "-" + "".join(random.choices(letters, k=6)), allow_unicode=False
            )
        return slug

    def save(self, *args, **kwargs):
        if self.world:
            self.world = self.world.strip()
        if not self.slug:
              self.slug = self.make_slug(self.world)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-pk", "world"]

