from django.db import models
import uuid


class Activity(models.Model):
                                   
    name        = models.CharField(max_length=80)
    description = models.TextField() 
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    id = models.UUIDField(primary_key=True, 
                          default=uuid.uuid4, 
                          editable=False)