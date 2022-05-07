from django.db import models
from django.shortcuts import reverse


from pytils.translit import slugify

def gen_slug(s):
    new_slug = slugify(s)
    return new_slug



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    author = models.TextField(blank=True, db_index=True)
    sections = models.ManyToManyField('Section', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)
    filename = models.CharField(max_length=150, db_index=True, unique=True)
    similardoc_filename = models.CharField(max_length=150, db_index=True)
    similardoc_title = models.CharField(max_length=150, db_index=True)


    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-date_pub']

class Section(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('section_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('section_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('section_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['id']
