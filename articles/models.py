from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


from ckeditor.fields import RichTextField
from unidecode import unidecode


def default_start_time():
	now = timezone.now()
	start = now.replace(hour=6, minute=0, second=0, microsecond=0)
	return start


class PublicManager(models.Manager):
	"""
	Returns published posts that are not in the future.
	"""

	def get_queryset(self):
		return super(PublicManager, self).get_queryset().filter(status='public', publish__lte=timezone.now())


class Tag(models.Model):
	"""Tag model. Many to many."""

	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'
		db_table = 'tag'
		ordering = ('title',)

	title = models.CharField(max_length=100, blank=True)
	slug = models.SlugField(unique=True)
	description = models.TextField(null=True, blank=True)
	is_active = models.BooleanField(default=True)
	seo_title = models.CharField(max_length=60, blank=True, null=True)
	seo_description = models.CharField(max_length=165, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return '/tag/{}/'.format(self.slug)


class Post(models.Model):
	""" Post model."""

	STATUS_CHOICES = (
		('draft', 'Draft'),
		('public', 'Public'),
	)

	LANGUAGE_CHOICES = (
		('PL', 'PL'),
		('EN', 'EN'),
	)

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
		db_table = 'post'
		ordering = ('-publish',)
		get_latest_by = 'date'

	objects = models.Manager()
	published = PublicManager()

	is_active = models.BooleanField(default=True)
	is_featured = models.BooleanField(default=False)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
	language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='PL')
	publish = models.DateTimeField(default=default_start_time)
	title = models.CharField(max_length=280)
	slug = models.SlugField(max_length=280, unique=True, blank=True, default='')
	content = RichTextField(blank=True, null=True)
	reading_time = models.IntegerField(blank=True, null=True)
	description = models.TextField(null=True, blank=True)
	seo_title = models.CharField(max_length=70, blank=True, null=True)
	seo_description = models.CharField(max_length=160, blank=True, null=True)

	post_image = models.ImageField(upload_to='post_images/', blank=True, null=True)
	post_thumb = models.ImageField(upload_to='post_thumbs/', blank=True, null=True)
	post_image_alt = models.CharField(max_length=280, null=True, blank=True)

	author = models.ForeignKey(User, blank=True, null=True, on_delete='SET_DEFAULT')

	tags = models.ManyToManyField(Tag, blank=True)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	# read_time = models.CharField(max_length=6, null=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			base_slug = slugify(unidecode(self.title))
			new_slug = base_slug
			counter = 0
			while Post.objects.filter(slug=new_slug).exists():
				counter += 1
				new_slug = '{}-cp-{}'.format(base_slug, str(counter))
				print(new_slug)

			self.slug = new_slug

		super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		if self.language == 'PL':
			absolute_url = '/pl/artykuly/{}'.format(self.slug)
			return absolute_url
		elif self.language == 'EN':
			absolute_url = '/articles/{}'.format(self.slug)
			return (absolute_url)
		else:
			return ''

	def get_url_for_social(self):
		if self.language == 'PL':
			absolute_url = 'https://tyrantsthem.com/pl/artykuly/{}'.format(self.slug)
			return absolute_url
		elif self.language == 'EN':
			absolute_url = 'https://tyrantsthem.com/articles/{}'.format(self.slug)
			return (absolute_url)
		else:
			return ''

