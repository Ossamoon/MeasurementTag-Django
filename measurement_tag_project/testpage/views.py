from django.shortcuts import render
from django.views.generic import TemplateView

class TestPage1(TemplateView):
    template_name = 'testpage1.html'

class TestPage2(TemplateView):
    template_name = 'testpage2.html'

class TestPage3(TemplateView):
    template_name = 'testpage3.html'
