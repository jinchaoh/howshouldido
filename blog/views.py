from django.shortcuts import render,render_to_response
from blog.models import Blog
# Create your views here.
def show_blog(request,blog_id):
    blog = Blog.objects.get(id = blog_id)
    print blog.title
    return render_to_response('blog.html',{'blog':blog})


    