from django.db import models
from datetime import datetime

# Create your models here.
from django.db import models
from datetime import datetime

class Investimento(models.Model):
    investimento = models.TextField(max_length=255)
    valores = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default =datetime.now)
    nivel = models.IntegerField(default=1)

