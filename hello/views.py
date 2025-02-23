from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def hello_json(request):
	return JsonResponse({"Message": "Hello World!"})

def hello_html(request):
	return render(request, 'hello/hello.html')

