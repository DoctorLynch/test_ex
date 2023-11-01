from django.db import models
from django.forms import DateTimeField

NULLABLE = {'blank': True, 'null': True}  # Используется, как указание - "Необязательный атрибут"


class Birds(models.Model):
    objects = None
    name = models.CharField(max_length=150, verbose_name='Название птицы')
    color_feather = models.CharField(max_length=150, verbose_name='Цвет перьев', **NULLABLE)
    image_bird = models.ImageField(upload_to='image', height_field=None, width_field=None, max_length=100, **NULLABLE)
    vision_attribute = models.BooleanField(default=False, verbose_name='Видел')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'Птица'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Птицы'  # Настройка для наименования набора объектов


class ViewBirds(models.Model):
    name = models.ForeignKey(Birds, on_delete=models.CASCADE, verbose_name='Название птицы')
    image_bird = models.ImageField(upload_to='image', height_field=None, width_field=None, max_length=100, **NULLABLE)
    number_of_views = models.IntegerField(default=0, verbose_name='количество просмотров')
    time_date_now = models.DateTimeField(**NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'Видел Птицу '  # Настройка для наименования одного объекта
        verbose_name_plural = 'Видел Птиц'  # Настройка для наименования набора объектов