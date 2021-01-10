from rest_framework.serializers import ModelSerializer
from .models import Post


class BlogSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields =['title', 'body', 'author', 'date_release']
