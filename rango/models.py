from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
	max = 128
	name = models.CharField(max_length=max, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
	
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural ='Categories'
	
	def __str__(self):  # For Python 2, use __unicode__ too
		return self.name

	def __unicode__(self):  # For Python 2, use __unicode__ too
		return self.name
	
class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	

	
	def __str__(self): 
		return self.title
		
	
	def __unicode__(self): 
		return self.title
		

class PageForm(models.Model):
	
	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')
		
		if url and not url.startswith('http://'):
			url = 'htttp://' + url
			cleaned_data['url'] + url
			
			return cleaned_data
	
