from django.shortcuts import render
from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'testpage.html'
