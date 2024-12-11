from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class GeneticTest(models.Model):
    animal_name = models.CharField(max_length=150, verbose_name='Имя животного')
    species = models.CharField(max_length = 150, verbose_name='Вид животного')
    test_date = models.DateField(verbose_name='Дата проведения теста')
    milk_yield = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='Продуктивность')
    health_status = models.CharField(max_length=150, verbose_name='Состояние здоровья')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.species = self.species.lower()
        return super().save(*args, **kwargs)
    
