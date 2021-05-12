from django.db       import models

class User(models.Model):
    email        = models.EmailField(max_length=200, unique=True)
    first_name   = models.CharField(max_length=255)
    last_name    = models.CharField(max_length=255)
    password     = models.CharField(max_length=255)
    phone        = models.CharField(max_length=255, blank=True)
    address      = models.CharField(max_length=255, blank=True)
    create_date  = models.DateTimeField(auto_now_add=True)
    update_date  = models.DateTimeField(auto_now=True)
    skin_type    = models.ForeignKey("SkinType", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'users'

class SkinType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'skin_types'