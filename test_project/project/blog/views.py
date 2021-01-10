from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from blog.models import Post

# Create your views here.
from blog.serializers import BlogSerializer


def post_page(request):
    return render(request, 'index.html', {'posts': Post.objects.all()})

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer

def post_app(request):
    return render(request, 'main_app.html')


