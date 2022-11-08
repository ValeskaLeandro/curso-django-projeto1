from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    # Representa o model que queremos encaixar aqui
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # Representa o id da linha do model descrito acima
    object_id = models.CharField()
    object_id = models.CharField(max_length=255)
    # Um campo que representa a relação genérica que conhece os
    # campos acima (content_type e object_id)
    content_object = GenericForeignKey('content_type', 'object_id')

    def save(self, *args, **kwargs):
        if not self.slug:
            ...
        return super().save(*args, **kwargs)
