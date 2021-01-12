from django.shortcuts import render

actions = actions.select_related('user', 'user__profile').prefetch_related('target')[:10]