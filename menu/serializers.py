from rest_framework import serializers
from .models import Item, Category, Menu

class ItemSerializer(serializers.ModelSerializer):

    # GET
    category = serializers.CharField(source='category.category_name', read_only=True)
    title = serializers.CharField(source='title.app_title', read_only=True)

    # POST
    add_category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True
    )
    add_title = serializers.PrimaryKeyRelatedField(
        queryset=Menu.objects.all(),
        write_only=True
    )

    class Meta:
        model = Item
        fields = [
            'id',
            'title',
            'add_title',
            'name',
            'description',
            'price',
            'rating',
            'image',
            'availability',
            'category',
            'add_category',
        ]
