from django.db import models

class ItemField(models.Model):
	content = models.CharField(max_length=1)

