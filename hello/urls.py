from django.urls import path
from .views import hello_json, hello_html

urlpatterns = [
	path('json/', hello_json, name='hello_json'),
	path('html/', hello_html, name='hello_html'),
]
