from django.db import models


class BaseModel(models.Model):
    created_dttm = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Создан')
    updated_dttm = models.DateTimeField(auto_now=True, editable=False, verbose_name='обновлен')

    class Meta:
        ordering = ['id']
        abstract = True
