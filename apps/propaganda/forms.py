# -*- encoding: utf-8 -*-

from django import forms
from .models import Propaganda

class PropagandaForm(forms.ModelForm):
	class Meta:
		model = Propaganda
		fields = "__all__"