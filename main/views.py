from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import *
from rest_framework import generics
from .models import *
from .serializers import *


class MainDashboard(ListView):
	model = ItemField
	template_name = 'main/base.html'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class ItemView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ItemField.objects.all()
	serializer_class = ItemFieldSerialize