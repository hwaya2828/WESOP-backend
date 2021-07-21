from django.db       import models

class User(models.Model):
    email         = models.EmailField(max_length=200, unique=True)
    first_name    = models.CharField(max_length=30)
    last_name     = models.CharField(max_length=30)
    password      = models.CharField(max_length=255)
    phone         = models.CharField(max_length=255, null=True)
    birth_day     = models.DateField(null=True)
    skin_type     = models.ForeignKey("SkinType", on_delete=models.CASCADE, null=True)
    refresh_token = models.CharField(max_length=255, null=True)
    create_at     = models.DateTimeField(auto_now_add=True)
    update_at     = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'

class SkinType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'skin_types'

class Address(models.Model):
    user    = models.ForeignKey("User", on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'address'
