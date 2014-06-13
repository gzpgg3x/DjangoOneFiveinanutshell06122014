# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib import auth
 
class Post(models.Model):
 
  title = models.CharField(max_length=255)
 
  machine_name = models.SlugField(max_length=255, primary_key=True)
 
  content = models.TextField(blank=True)
 
  publication_date = models.DateTimeField(auto_now_add=True)

  owner = models.ForeignKey(auth.models.User)
 
  def __unicode__(self):
    return self.title
 
  def excerpt(self):
    return self.content[:300] + u'…'
 
  class Meta:
    ordering = [u'-publication_date']

  def get_absolute_url(self):
    from django.core.urlresolvers import reverse
    return reverse('postdetails',kwargs={ 'slug':self.machine_name })  

class Commentary(models.Model):
  post = models.ForeignKey(Post)
 
  content = models.TextField()
 
  publication_date = models.DateTimeField(auto_now_add=True)
 
  author = models.CharField(max_length=50, default=u'The invisible man')
 
  def __unicode__(self):
    return self.owner + u'@' + unicode(self.post)
 
  class Meta:
    verbose_name_plural = u'commentaries'
    ordering = [u'-publication_date']

