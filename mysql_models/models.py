from django.db import models


class IndexProduct(models.Model):
    id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.product_name

    class Meta:
        managed = False
        db_table = 'index_product'


class IndexImage(models.Model):
    id = models.IntegerField(primary_key=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_image'
