# -*- encoding: utf-8 -*-
from django.views.generic import ListView, TemplateView
from djangoblog.forms import SearchForm
from posts.forms import AddCommentaryForm
from posts.models import Post
 
class PostList(ListView):
    template_name = 'postlist.html'
    model = Post

# added for the section "The post view"
class PostDetails(TemplateView):
  template_name = 'postdetails.html'
 
  def post(self, request, *args, **kwargs):
    return self.get(request, *args, **kwargs)
 
  # Overriding
  def get_context_data(self, **kwargs):
    context = super(PostDetails, self).get_context_data(**kwargs)
 
    post = self.get_post(kwargs['slug'])
    form = self.get_form(post)
 
    context.update({'form':form, 'post':post})
 
    return context
 
  # Helper
  def get_post(self, slug):
    return Post.objects.get(pk=slug)
 
  # Helper
  def get_form(self, post):
    if self.request.method == 'POST':
      form = AddCommentaryForm(self.request.POST)
      if form.is_valid():
        commentary = form.save(commit=False)
        post.commentary_set.add(commentary)
      else:
        return form
 
    return AddCommentaryForm()

class SearchResults(ListView):
  template_name = "searchresults.html"
 
  # Override
  def get_queryset(self):
    if self.request.method == 'GET':
      form = SearchForm(self.request.GET)
      if form.is_valid():
        query = form.cleaned_data['query']
        results = Post.objects.filter(content__icontains=query)
        return results
 
    return Post.objects.none()
  
  # def get_queryset(self):
  # from django.db.models import Q
  # if self.request.method == 'GET':
  #   form = SearchForm(self.request.GET)
  #   if form.is_valid():
  #     query = form.cleaned_data['query']
  #     words = query.split(' ')
  #     qobjects = [Q(content__icontains=w) | Q(title__icontains=w) for w in words]
  #     condition = reduce(lambda x,y: x & y, qobjects)
  #     results = Post.objects.filter(condition)
  #     return results
 
  # return Post.objects.none() 
