from django.shortcuts import get_object_or_404
from rest_framework import serializers

from cars.models import Car, Comment


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["content", "created_at", "author"]

    def create(self, validated_data):
        validated_data["author"] = self.context['request'].user
        validated_data["car"] = get_object_or_404(Car, pk=self.context['pk'])
        return super().create(validated_data)


class CarSerializer(serializers.ModelSerializer):
    """Сериализатор для автомобилей."""

    owner = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Car
        fields = ["make",
                  "model",
                  "year",
                  "description",
                  "created_at",
                  "updated_at",
                  "owner",
                  "comments"]

    def create(self, validated_data):
        validated_data["owner"] = self.context['request'].user
        return super().create(validated_data)
