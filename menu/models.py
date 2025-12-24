from django.db import models

class Menu(models.Model):
    app_title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models. DateTimeField(auto_now=True)

    def __str__(self):
        return self.app_title
    
class Category(models.Model):
    category_name = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models. DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
    

class Item(models.Model):
    title = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='title')
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    rating = models.FloatField(blank=True, null=True)
    image = models.URLField()
    availability = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models. DateTimeField(auto_now=True)

    def __str__(self):
        return self.name