from django.db import models


class Food(models.Model):

    name    = models.CharField(max_length=80)

    total_protein_g = models.DecimalField(max_digits=8, decimal_places=2)
    total_carb_g    = models.DecimalField(max_digits=8, decimal_places=2)

    total_sat_fat_g   = models.DecimalField(max_digits=8, decimal_places=2)
    total_unsat_fat_g = models.DecimalField(max_digits=8, decimal_places=2)
    
    total_kcal = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_g = models.DecimalField(max_digits=8, decimal_places=2)
