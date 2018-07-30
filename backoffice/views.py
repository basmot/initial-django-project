from django.contrib import messages
from django.shortcuts import render
from django.utils.safestring import mark_safe


def home(request):
    return render(request, template_name='home.html')


def add_message(request, level, message):
    map_font_level = {
        messages.SUCCESS: '<i class="fas fa-check-circle"></i>',
        messages.INFO: '<i class="fas fa-info-circle"></i>',
        messages.WARNING: '<i class="fas fa-exclamation-triangle"></i>',
        messages.ERROR: '<i class="fas fa-exclamation-circle"></i>',
    }
    message = '{} {}'.format(map_font_level.get(level, ''), message)
    messages.add_message(request, level, mark_safe(message))
