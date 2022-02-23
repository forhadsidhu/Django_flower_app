from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from imagekit.models import ImageSpecField # < here
from pilkit.processors import ResizeToFill # for imageprocessing

# Adding tag model
class Tag(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # < here
        self.slug = slugify(self.title)
        super(Tag, self).save()

    def get_absolute_url(self):
        # reverse method gives cannonical url like http:12.1.0.1 then we just prove slug field in this url
        # then it will be like http:12.1.0./title
        return reverse('tags', args=[str(self.slug)])


# Add a category class and a category field
class Category(models.Model):
    title = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title


class Flower(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    slug = models.SlugField(blank=True, default='')
    # Add category field as Many2one field
    # on_delete=models.PROTECT prevents the deletion of a Category object if it’s
    # referenced by a Flower object:
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    # Adding tags as many2many field
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(default='', blank=True, upload_to = 'images')
    image_thumbnail = ImageSpecField(source='image', #original image
                                     processors=[ResizeToFill(350, 200)],
                                     format='JPEG',
                                     options={'quality': 60})  # < her
    #Using the original uploaded images can result in very heavy pages. For example
# Amelanchier_asiatica5.jpg that I used for testing was 4.3MB. Image processing
# reduced that size to 18.2KB!
# ImageSpecField is similar to ImageField but it automatically applies the image
# processing we specify:

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Slugify function converts strings to URL slugs
        self.slug = slugify(self.title)
        super(Flower, self).save()

    # We can add a “View on site” link to the admin by defining a get_absolute_url
    # method
    def get_absolute_url(self):
        # reverse method gives cannonical url like http:12.1.0.1 then we just prove slug field in this url
        # then it will be like http:12.1.0./title
        return reverse('detail', args=[str(self.slug)])
