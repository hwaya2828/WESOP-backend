from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'menus'
    
class Category(models.Model):
    menu              = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name              = models.CharField(max_length=255)
    description_title = models.CharField(max_length=255, blank=True)
    description       = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'categories'
    
class Product(models.Model):
    category          = models.ForeignKey("Category", on_delete=models.CASCADE)
    name              = models.CharField(max_length=255)
    summary           = models.CharField(max_length=255)
    thumbnail_url     = models.CharField(max_length=2000)
    description       = models.TextField()
    content           = models.TextField()
    content_image_url = models.CharField(max_length=2000)
    count             = models.IntegerField(default=0)
    feature           = models.ManyToManyField('Feature', through='ProductFeature')
    ingredient        = models.ManyToManyField('Ingredient', through='ProductIngredient')

    class Meta:
        db_table = 'products'

class ProductSelection(models.Model):
    product   = models.ForeignKey("Product", on_delete=models.CASCADE)
    size      = models.CharField(max_length=255)
    price     = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=2000)

    class Meta:
        db_table = 'product_selections'

class FeatureCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'feature_categories'

class Feature(models.Model):
    feature_category = models.ForeignKey("FeatureCategory", on_delete=models.CASCADE)
    name             = models.CharField(max_length=255)
 
    class Meta:
        db_table = 'features'

class ProductFeature(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    feature = models.ForeignKey("Feature", on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_features'

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'ingredients'

class ProductIngredient(models.Model):
    product    = models.ForeignKey("Product", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("Ingredient", on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_ingredients'