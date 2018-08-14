# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import RegisterUserForm
# Create your views here.

class RegisterUserView(CreateView):
	form_class = RegisterUserForm
	template_name = "register.html"

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return HttpResponseForbidden()
		return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		user = form.save(commit=False)
		user.set_password(form.cleaned_data['password1'])
		user.save()
		return HttpResponse('User Registered')


