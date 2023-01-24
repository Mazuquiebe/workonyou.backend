from django.db import models
import uuid


class Meal(models.Model):

    protein_grams   = models.DecimalField(max_digits=6, decimal_places=2)
    carb_grams      = models.DecimalField(max_digits=6, decimal_places=2)
    sat_fat_grams   = models.DecimalField(max_digits=6, decimal_places=2)
    unsat_fat_grams = models.DecimalField(max_digits=6, decimal_places=2)
    total_kcal      = models.DecimalField(max_digits=6, decimal_places=2)

    # ingredients   = models.ManyToManyField('feed.Food')
    
    user = models.OneToOneField('users.User', 
                                related_name='meals',
                                on_delete=models.CASCADE)

    id   = models.UUIDField(primary_key=True, 
                            default=uuid.uuid4, 
                            editable=False)
