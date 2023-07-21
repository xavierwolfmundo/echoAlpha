from rest_framework import serializers
from .models import Post, Comment, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    tags = TagSerializer(many=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'author', 'categories', 'tags', 'comments']

    def create(self, validated_data):
        categories_data = validated_data.pop('categories', [])
        tags_data = validated_data.pop('tags', [])
        post = Post.objects.create(**validated_data)

        for category_data in categories_data:
            category, _ = Category.objects.get_or_create(**category_data)
            post.categories.add(category)

        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            post.tags.add(tag)

        return post
