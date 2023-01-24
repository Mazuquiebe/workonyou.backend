from django.db import models
import uuid


class SuggestedDiet(models.Model):

    id                  = models.UUIDField(primary_key=True, default=uuid.uuid4)
    suggested_protein   = models.DecimalField(max_digits=8, decimal_places=1)
    suggested_carb      = models.DecimalField(max_digits=8, decimal_places=1)
    suggested_sat_fat   = models.DecimalField(max_digits=8, decimal_places=1)
    suggested_unsat_fat = models.DecimalField(max_digits=8, decimal_places=1)
    suggested_water     = models.DecimalField(max_digits=8, decimal_places=1)
    basal_metabolism    = models.DecimalField(max_digits=8, decimal_places=1)

    user = models.OneToOneField('users.User',
                                related_name='suggested_diet', 
                                on_delete=models.CASCADE)