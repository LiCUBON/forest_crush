from rest_framework import serializers
from .models import *

class ItemFieldSerialize(serializers.ModelSerializer):
	class Meta:
		model = ItemField
		fields = ('content',)