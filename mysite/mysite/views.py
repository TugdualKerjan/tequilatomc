from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def fail(request):
    return HttpResponse("An error occured with the authentication")